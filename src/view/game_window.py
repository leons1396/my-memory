import tkinter as tk
import random


class GameWindow(tk.Toplevel):
    def __init__(self, controller, parent):
        super().__init__(parent)
        # self.parent = parent
        self.controller = controller

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
        self.frame_cards = tk.Frame(self)
        # max 5 columns per row
        self.cards = []
        half_cards = int(num_cards / 2)
        # the outer loop is necessary to create pairs of cards
        positions = []
        card_values = [value for _ in range(0, 2) for value in range(0, half_cards)]
        random.shuffle(card_values)
        card_idx = 0
        for i in range(0, 2):
            # multiplier to get desired rows and cols
            for num_card in range(0, half_cards):
                # TODO set cards randomly on the grid
                # num_card is later the image
                row = (num_card + half_cards * i) // 5
                column = (num_card + half_cards * i) % 5
                card_value = card_values.pop(0)
                positions.append((row, column, card_value, card_idx))
                card_idx += 1

        # set cards to the grid later. iter trough all shuffeled row and col pairs
        # random.shuffle(positions)
        # pos = tuple(row, col, card number, idx)
        for pos in positions:
            card = tk.Button(
                self.frame_cards,
                text=f"Card{pos[3]}",
                command=lambda card_idx=pos[3]: self.show_card(card_idx),
            )
            # tuple(card, value)
            self.cards.append((card, pos[2]))
            card.grid(row=pos[0], column=pos[1], ipadx=60, ipady=60, padx=10, pady=5)

        # sort the cards list by the idx
        # self.cards.sort(key=lambda x: x[2])
        print("Cards: ", self.cards)
        self.frame_cards.grid(row=1, column=0)

    def show_card(self, idx_card):
        # turn button into image
        print(f"Show card with index: {idx_card}")
        # show value of the card
        card_value = self.cards[idx_card][1]
        print(f"Card value of selected card: {card_value}")
        # change card text to image
        self.cards[idx_card][0].config(text=f"'Image_{self.cards[idx_card][1]}'")

    def hide_card(self, idx_card):
        # somehow pass the idx_card from the show_card function to this function
        pass
