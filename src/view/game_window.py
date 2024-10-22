import tkinter as tk


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
        # TODO use frame to set the cards
        self.create_cards(num_cards)
        # ========================== Labels ============================
        self.lbl_rem_pairs = tk.Label(self, text="Remaining pairs: ")
        self.lbl_rem_pairs.grid(row=0, column=0)

        # set player names in another frame
        self.frame_players = tk.Frame(self)
        for i, player in enumerate(player_names):
            tk.Label(self.frame_players, text=player).grid(row=i, column=0)
        self.frame_players.grid(row=2, column=0)
        # ========================== Entries ============================
        self.txt_rem_pairs = tk.Entry(self)
        self.txt_rem_pairs.grid(row=0, column=1)

    def create_cards(self, num_cards):
        self.frame_cards = tk.Frame(self)
        # max 5 columns per row
        self.cards = []
        for num_card in range(0, num_cards):
            row = num_card // 5
            column = num_card % 5
            card = tk.Button(
                self.frame_cards,
                text=f"Card{num_card}",
                command=lambda idx_card=num_card: self.show_card(idx_card),
            )
            self.cards.append(card)
            card.grid(row=row, column=column, ipadx=60, ipady=60, padx=10, pady=5)

        self.frame_cards.grid(row=1, column=0)

    def show_card(self, idx_card):
        # turn button into image
        print(f"Show card {idx_card}")
        self.cards[idx_card].config(text="X")
