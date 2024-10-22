class Model:
    def __init__(self):
        self.game_window_is_open = False
        self.difficulty_level = None  # values are "easy", "medium", "hard"

    def set_difficulty_level(self, lvl):
        self.difficulty_level = lvl
