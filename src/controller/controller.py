import sys
import tkinter as tk

sys.path.append("C:/Users/Leon/Documents/programming/MY-MEMORY")
from src.view import game_window


class Controller:
    def __init__(self, model, main_window):
        print("new controller")
        self.model = model
        self.main_window = main_window

    def start(self):
        self.main_window.create_start_window()

    def create_game_window(self):
        # make sure only one game window is open
        if not self.model.game_window_is_open:
            print("Create game window")
            # self = controller itself
            self.game_window = game_window.GameWindow(self, self.main_window)
            self.game_window.create_game_window()
            self.model.game_window_is_open = True

            # hide the start/root window
            self.main_window.withdraw()
        else:
            print("Game window already exists")

    def delete_game_window(self):
        # show the start/root window
        self.main_window.deiconify()
        self.game_window.destroy()
        self.model.game_window_is_open = False

    def set_difficulty_lvl(self, lvl):
        self.model.set_difficulty_level(lvl)
        self.main_window.set_difficulty_level(lvl)
