import copy


class Model:
    def __init__(self):
        self.game_window_is_open = False
        self.difficulty_level = None  # values are "easy", "medium", "hard"
        self.player_names = None  # list of player names
        self.card_values = None
        self.count_open_cards = 0
        self.temp_card_idx = []
        self.count_player = 0

    def set_difficulty_level(self, lvl: str):
        self.difficulty_level = lvl

    def set_player_names(self, num_players: list):
        self.player_names = copy.deepcopy(num_players)

    def set_card_values(self, card_values: list):
        self.card_values = card_values

    def set_temp_card_idx(self, card_idx: int):
        # temporarily store the card_idx
        self.temp_card_idx.append(card_idx)

    def get_game_setting(self) -> dict:
        return {
            "num_cards": {"easy": 12, "medium": 16, "hard": 20}[self.difficulty_level],
            "num_players": len(self.player_names),
            "player_names": self.player_names,
        }

    def get_temp_card_idx(self) -> list:
        return self.temp_card_idx

    def are_two_cards_open(self) -> bool:
        self.count_open_cards += 1
        print("Counter increased: ", self.count_open_cards)
        if self.count_open_cards == 2:
            return True
        return False

    def check_pair(self) -> bool:
        # two cards are open and check if it is a match
        if (
            self.card_values[self.temp_card_idx[0]]
            == self.card_values[self.temp_card_idx[1]]
        ):
            print("Pair found")
            return True
        else:
            print("No pair found")
            return False

    def clean_round(self):
        self.temp_card_idx.clear()
        self.count_open_cards = 0

    def get_player(self):
        return (self.player_names[self.count_player], self.count_player)

    def next_player(self, change_player: bool):
        # current player has found a pair he can continue
        if not change_player:
            return
        # max players len(self.player_names)
        if len(self.player_names) == 1:
            # only one player
            self.count_player = 0
        elif self.count_player == len(self.player_names) - 1:
            # start from beginning
            self.count_player = 0
        else:
            # take next player
            self.count_player += 1
