from board import Board
from game_manager import GameManager
from game_controller import GameController
from disk import Disk

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLUMNS = 8
SPACING = 100
counter_1 = 60
RESET_COUNTER_1 = 60
counter_2 = 30
RESET_COUNTER_2 = 30
BACKGROUND = (30, 113, 30)

board = Board(ROWS, COLUMNS, SPACING)
gm = GameManager(board)
gc = GameController(board, gm, WIDTH, HEIGHT)


def setup():
    size(WIDTH, HEIGHT)
    background(*BACKGROUND)


def draw():
    global counter_1, counter_2
    board.display()
    gc.end_game()
    if gc.game_ends:
        # delays the window popping so that it
        # doesn't stop the drawing process
        if counter_2 != 0:
            counter_2 -= 1
        elif gc.call_store_method:
            gc.store_score("scores.txt")
            counter_2 = RESET_COUNTER_2
    gc.end_game()

    if gm.turn is False:
        # delays the AI
        if counter_1 != 0:
            counter_1 -= 1
        else:
            gm.ai_make_move()
            counter_1 = RESET_COUNTER_1


def mousePressed():
    if gm.turn is True:
        gm.player_make_move(mouseX, mouseY)
