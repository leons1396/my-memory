import sys
import tkinter as tk

sys.path.append("C:/Users/Leon/Documents/programming/MY-MEMORY")
from src.view.main_window import MainWindow
from src.model.model import Model
from src.controller.controller import Controller


def main():
    root = MainWindow()
    model = Model()
    controller = Controller(model, root)
    root.set_controller(controller)
    controller.start()
    root.mainloop()


if __name__ == "__main__":
    main()
