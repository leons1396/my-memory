import tkinter as tk


class GameWindow(tk.Toplevel):
    def __init__(self, controller, parent):
        super().__init__(parent)
        # self.parent = parent
        self.controller = controller
        self.game_window_exists = False

    def create_memory_window(self):
        self.game_window_exists = True
        self.geometry("600x600")
        self.title("Playboard")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        # close the application
        self.btn_quit = tk.Button(
            self, text="Back", command=self.delete_game_window
        ).grid(row=2, column=0, ipadx=20)

    def delete_game_window(self):
        self.game_window_exists = False
        self.destroy()
