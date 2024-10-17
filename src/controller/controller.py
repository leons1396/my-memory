import sys
import tkinter as tk

sys.path.append("C:/Users/Leon/Documents/programming/MY-MEMORY")
from src.view import game_window


class Controller:
    def __init__(self, model, main_window):
        print("new controller")
        self.model = model
        self.main_window = main_window
        self.memory_window = game_window.GameWindow(self, self.main_window)

    def start(self):
        self.main_window.create_start_window()

    def create_memory_window(self):
        # self = controller itself
        if not self.memory_window.game_window_exists:
            print("Create game window")
            self.memory_window.create_memory_window()
        else:
            print("Game window already exists")
