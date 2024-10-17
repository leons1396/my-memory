import tkinter as tk
import sys

sys.path.append("C:/Users/Leon/Documents/programming/MY-MEMORY")
from src.view import game_window


class MainWindow(tk.Tk):
    """It serves as the root/parent window for the application."""

    def __init__(self):
        super().__init__()
        self.controller = None
        self.start_window = None

    def set_controller(self, controller):
        self.controller = controller

    def create_start_window(self):
        self.geometry("600x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        self.btn_start = tk.Button(
            self, text="Start", command=self.controller.create_memory_window
        ).grid(row=1, column=0, ipadx=20)
        self.btn_quit = tk.Button(self, text="Quit", command=self.quit).grid(
            row=2, column=0, ipadx=20
        )
