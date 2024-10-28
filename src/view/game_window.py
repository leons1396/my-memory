import tkinter as tk
import tkinter.messagebox as messagebox
import random
from PIL import Image, ImageTk
import os
import sys

sys.path.append("C:/Users/Leon/Documents/programming/my-memory")
from src import secrets


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
        self.geometry("900x900")
        self.title("Playboard")
        self.images = self.load_images()
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
        self.lbl_rem_pairs = tk.Label(
            self.frame_rem_pairs,
            text="Remaining pairs: ",
            font=("Arial", 20, "bold"),
            fg="blue",
        )
        self.lbl_num_rem_pairs = tk.Label(
            self.frame_rem_pairs,
            text=int(num_cards / 2),
            font=("Arial", 20, "bold"),
            fg="blue",
        )
        self.lbl_rem_pairs.grid(row=0, column=0)
        self.lbl_num_rem_pairs.grid(row=0, column=1, sticky=tk.W)
        self.frame_rem_pairs.grid(row=0, column=0, sticky=tk.W)

        # set player names in another frame
        self.frame_players = tk.Frame(self)
        self.lbl_players = []
        self.lbl_num_pairs_players = []
        for i, player in enumerate(player_names):
            lbl = tk.Label(self.frame_players, text=player, font=("Arial", 20, "bold"))
            lbl_num = tk.Label(
                self.frame_players, text="0", font=("Arial", 20, "bold"), bg="yellow"
            )
            self.lbl_players.append(lbl)
            self.lbl_num_pairs_players.append(lbl_num)
            lbl.grid(row=i, column=0)
            lbl_num.grid(row=i, column=1)
        self.frame_players.grid(row=2, column=0, sticky=tk.W)

        # ========================== Entries ============================

    def load_images(self):
        imgs = []
        src = secrets.SECRETS["PATH"]["IMG_RESIZED"]
        for img in os.listdir(path=secrets.SECRETS["PATH"]["IMG_RESIZED"]):
            pil_image = Image.open(os.path.join(src, img))
            imgs.append(ImageTk.PhotoImage(pil_image))
        return imgs

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
            card.grid(row=pos[0], column=pos[1], ipadx=40, ipady=40, padx=10, pady=5)

        self.frame_cards.grid(row=1, column=0)

    def show_card(self, idx_cards: list) -> None:
        # turn button into image
        # print(f"Show card with index: {idx_cards}")
        # show value of the card
        # change card text to image
        # TODO Later, I think it is different to handle the images, for now test it with values
        # card values are numbers from 0 to num_cards/2. Card value corresponds to a image
        # for idx in idx_cards:
        #     self.cards[idx].config(text=f"'Image_{self.card_values[idx]}'")
        for idx in idx_cards:
            self.cards[idx].config(image=self.images[self.card_values[idx]])

    def close_cards(self, idx_cards: list) -> None:
        for idx in idx_cards:
            self.cards[idx].config(text=f"'Card_{idx}'", image="")

    def deactivate_cards(self, idx_cards: list) -> None:
        for idx in idx_cards:
            self.cards[idx].config(state="disabled")
            # self.cards[idx].config(relief="sunken")

    def show_player(self, player_name: str, player_idx: int) -> None:
        # show the player name
        messagebox.showinfo(title="Info", message=f"Player {player_name}'s turn")
        # highlight the current player name
        for i, lbl in enumerate(self.lbl_players):
            # find the corresponding label on the grid to the player whose turn it is
            if i == player_idx:
                lbl.config(fg="green")
            else:
                lbl.config(fg="black")

    def update_player_score(self, player_idx: int, score: int) -> None:
        self.lbl_num_pairs_players[player_idx].config(text=str(score))

    def update_remaining_score(self) -> None:
        rem_pairs = int(self.lbl_num_rem_pairs.cget("text"))
        rem_pairs -= 1
        self.lbl_num_rem_pairs.config(text=str(rem_pairs))
