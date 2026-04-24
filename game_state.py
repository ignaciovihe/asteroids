from enum import Enum

class GameState(Enum):
    PLAYING = "playing"
    GAME_OVER = "game_over"
    ENTER_NAME = "enter_name"
    DISPLAY_SCORE = "display_score"
    EXIT = "exit"
    RESET = "reset"