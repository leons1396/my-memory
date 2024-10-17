# import sys
import tkinter as tk

# sys.path.append("C:/Users/Leon/Documents/programmingcode/MY-MEMORY")
from controller import controller as ctrl


def main():
    root = tk.Tk()
    game = ctrl.Controller(root)
    root.mainloop()


if __name__ == "__main__":
    main()
