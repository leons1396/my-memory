import sys
import tkinter as tk

sys.path.append("C:/Users/Leon/Documents/programming/MY-MEMORY")
from src.model import model
from src.view import view


class Controller:
    def __init__(self, parent):
        self.model = model.Model()
        self.view = view.View(parent)
