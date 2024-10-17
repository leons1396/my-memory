import tkinter as tk
import sys

sys.path.append("C:/Users/Leon/Documents/programming/MY-MEMORY")
from src.view import start_window
from src.view import game_window


class View:
    def __init__(self, parent):
        # super().__init__(parent)
        self.parent = parent
        self.parent.title("My Memory")

        # start = start_window.StartWindow(self.parent)
        btn_start = tk.Button(
            self.parent, text="Start", command=self.create_start_window
        ).pack()
        btn_quit = tk.Button(self.parent, text="Quit", command=self.parent.quit).pack()

    def create_start_window(self):
        start = start_window.StartWindow(self.parent)
