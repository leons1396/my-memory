import tkinter as tk


class StartWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.transient(parent)
        self.title("Start Window Child")
        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button.pack(side="top")
