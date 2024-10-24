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
            self.model.set_player_names(self.main_window.get_player_names_from_user())
            print("++++ game setting model", self.model.get_game_setting())
            self.game_window.create_game_window(**self.model.get_game_setting())
            self.model.game_window_is_open = True
            # set the randomly assigned card values to the model
            self.model.set_card_values(self.game_window.get_card_values())

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

    def play_round(self, card_idx):
        print("Click on Card")
        # check if the card is already open
        if card_idx not in self.model.get_temp_card_idx():
            print("Set temp card idx")
            self.model.set_temp_card_idx(card_idx)
        else:
            # continue
            # TODO some kind of message to the user???
            print("Card already open")
            return

        if self.model.are_two_cards_open():
            self.game_window.show_card(self.model.get_temp_card_idx())
            self.game_window.update()
            if self.model.check_pair():
                # pair found
                self.update_scores()
                self.game_window.deactivate_cards(self.model.get_temp_card_idx())
            else:
                # no pair found
                self.game_window.after(
                    2000, self.game_window.close_cards(self.model.get_temp_card_idx())
                )
            self.model.clean_round()
        else:
            # only one card is open, continue
            self.game_window.show_card(self.model.get_temp_card_idx())
            return

    def update_scores(self):
        pass
