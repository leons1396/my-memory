import copy


class Model:
    def __init__(self):
        self.game_window_is_open = False
        self.difficulty_level = None  # values are "easy", "medium", "hard"
        self.player_names = None  # list of player names

    def set_difficulty_level(self, lvl):
        self.difficulty_level = lvl

    def set_player_names(self, num_players: list):
        self.player_names = copy.deepcopy(num_players)

    def get_game_setting(self):
        return {
            "num_cards": {"easy": 12, "medium": 16, "hard": 20}[self.difficulty_level],
            "num_players": len(self.player_names),
            "player_names": self.player_names,
        }
