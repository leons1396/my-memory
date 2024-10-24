import tkinter as tk
import random


class GameWindow(tk.Toplevel):
    def __init__(self, controller, parent):
        super().__init__(parent)
        # self.parent = parent
        self.controller = controller
        self.card_values = []

    def get_card_values(self):
        return self.card_values

    def create_game_window(self, num_cards, num_players, player_names):
        # TODO may set the size based on the number of cards
        self.geometry("1500x1500")
        self.title("Playboard")

        # ========================== Buttons ============================
        # close the application
        self.btn_quit = tk.Button(
            self, text="Back", command=self.controller.delete_game_window
        )
        # TODO set row and column dynamically based on the number of cards and players
        self.btn_quit.grid(row=10, column=1, ipadx=20)

        # memory cards
        print("Number of Cards: ", num_cards)
        print("Number of players game window: ", num_players)
        print("Player names game window: ", player_names)
        self.create_cards(num_cards)
        # ========================== Labels ============================
        self.frame_rem_pairs = tk.Frame(self)
        self.lbl_rem_pairs = tk.Label(self.frame_rem_pairs, text="Remaining pairs: ")
        self.lbl_rem_pairs.grid(row=0, column=0)

        # set player names in another frame
        self.frame_players = tk.Frame(self)
        for i, player in enumerate(player_names):
            tk.Label(self.frame_players, text=player).grid(row=i, column=0)
        self.frame_players.grid(row=2, column=0, sticky=tk.W)

        # ========================== Entries ============================
        self.txt_rem_pairs = tk.Entry(self.frame_rem_pairs)
        self.txt_rem_pairs.grid(row=0, column=1)
        self.frame_rem_pairs.grid(row=0, column=0, sticky=tk.W)

    def create_cards(self, num_cards):
        """Create the memory grid with the desired number of cards. The values for each
        card are randomly assigned. There are half as many unique values as cards, to
        create pairs of cards."""
        self.frame_cards = tk.Frame(self)
        # max 5 columns per row
        self.cards = []
        half_cards = int(num_cards / 2)
        # the outer loop is necessary to create pairs of cards
        positions = []
        _card_values = [value for _ in range(0, 2) for value in range(0, half_cards)]
        random.shuffle(_card_values)

        card_idx = 0
        for i in range(0, 2):
            # multiplier to get desired rows and cols
            for num_card in range(0, half_cards):
                # num_card is later the image
                row = (num_card + half_cards * i) // 5
                column = (num_card + half_cards * i) % 5
                card_value = _card_values.pop(0)
                positions.append((row, column, card_value, card_idx))
                card_idx += 1

        # set cards to the grid later. iter trough all shuffeled row and col pairs
        # pos = tuple(row, col, card number, idx)
        for pos in positions:
            card = tk.Button(
                self.frame_cards,
                text=f"Card{pos[3]}",
                command=lambda card_idx=pos[3]: self.controller.play_round(card_idx),
            )
            # tuple(card, value)
            self.cards.append(card)
            self.card_values.append(pos[2])
            card.grid(row=pos[0], column=pos[1], ipadx=60, ipady=60, padx=10, pady=5)

        self.frame_cards.grid(row=1, column=0)

    def show_card(self, idx_cards: list) -> None:
        # turn button into image
        print(f"Show card with index: {idx_cards}")
        # show value of the card
        # change card text to image
        # TODO Later, I think it is different to handle the images, for now test it with values
        for idx in idx_cards:
            self.cards[idx].config(text=f"'Image_{self.card_values[idx]}'")

    def close_cards(self, idx_cards: list) -> None:
        for idx in idx_cards:
            self.cards[idx].config(text=f"'Card_{idx}'")

    def deactivate_cards(self, idx_cards: list) -> None:
        for idx in idx_cards:
            self.cards[idx].config(state="disabled")
            # self.cards[idx].config(relief="sunken")
