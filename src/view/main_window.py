import tkinter as tk
from tkinter import messagebox
import sys

sys.path.append("C:/Users/Leon/Documents/programming/MY-MEMORY")
from src.view import game_window


class MainWindow(tk.Tk):
    """It serves as the root/parent window for the application."""

    def __init__(self):
        super().__init__()
        self.controller = None
        self.lbl_num_players = tk.StringVar()
        self.lbl_num_players.set("1")

    def set_controller(self, controller):
        self.controller = controller

    def create_start_window(self):
        MAX_PLAYERS = 4
        self.geometry("300x300")
        # self.columnconfigure(4, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(6, weight=1)

        # ========================== Buttons ============================
        self.btn_minus = tk.Button(self, text="-", command=self.decrease)
        self.btn_minus.grid(row=1, column=3)

        self.btn_plus = tk.Button(self, text="+", command=self.increase)
        self.btn_plus.grid(row=1, column=4)

        self.btn_start = tk.Button(
            self, text="Start", command=self.controller.create_game_window
        )
        self.btn_start.grid(row=7, column=2, ipadx=20)

        self.btn_quit = tk.Button(self, text="Quit", command=self.quit)
        self.btn_quit.grid(row=8, column=2, ipadx=20)

        # ========================== Labels ============================
        self.lbl_title_num_players = tk.Label(self, text="Number of players")
        self.lbl_title_num_players.grid(row=1, column=0)

        self.lbl_show_num_players = tk.Label(self, textvariable=self.lbl_num_players)
        self.lbl_show_num_players.grid(row=1, column=1)

        self.lbl_players = [
            tk.Label(self, text=f"Player {i}") for i in range(1, MAX_PLAYERS + 1)
        ]
        for i, lbl_player in enumerate(self.lbl_players, 0):
            lbl_player.grid(row=2, column=i)

        # ========================== Entries ============================
        self.txt_players = [tk.Entry(self) for i in range(MAX_PLAYERS)]
        for i, txt_player in enumerate(self.txt_players, 0):
            txt_player.grid(row=3, column=i)
        self.update_player_from_board(count=int(self.lbl_num_players.get()))

    def increase(self):
        """Increase the number of players by 1 controlled by the plus button."""
        self.update()
        count = int(self.lbl_num_players.get())
        if count < 4:
            new_count = count + 1
            self.lbl_num_players.set(new_count)
            self.update_player_from_board(new_count)
        else:
            messagebox.showinfo(title="Info", message="Max number of players reached")

    def decrease(self):
        """Decrease the number of players by 1 controlled by the minus button."""
        # update label num_players
        self.update()
        count = int(self.lbl_num_players.get())
        if count > 1:
            new_count = count - 1
            self.lbl_num_players.set(new_count)
            self.update_player_from_board(new_count)
        else:
            messagebox.showinfo(
                title="Info", message="Number of players have to be greater than 1"
            )

    def update_player_from_board(self, count):
        """Enables and disables the player labels and entry fields based on the
        number of players."""
        for i, (lbl_player, txt_player) in enumerate(
            zip(self.lbl_players, self.txt_players), 1
        ):
            if i <= count:
                lbl_player.config(state="normal")
                txt_player.config(state="normal")
            else:
                lbl_player.config(state="disabled")
                txt_player.config(state="disabled")
