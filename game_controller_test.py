from game_controller import GameController
from game_manager import GameManager
from board import Board


def test_constructor():
    board_1 = Board(2, 2, 100)
    gm_1 = GameManager(board_1)
    gc_1 = GameController(board_1, gm_1, 200, 200)
    assert gc_1.board == board_1
    assert gc_1.gm == gm_1
    assert gc_1.WIDTH == 200
    assert gc_1.HEIGHT == 200
    assert gc_1.black_count == 0
    assert gc_1.call_store_method
    assert not gc_1.new_high_score
    assert not gc_1.game_ends

    board_2 = Board(4, 4, 100)
    gm_2 = GameManager(board_2)
    gc_2 = GameController(board_2, gm_2, 400, 400)
    assert gc_2.board == board_2
    assert gc_2.gm == gm_2
    assert gc_2.WIDTH == 400
    assert gc_2.HEIGHT == 400
    assert gc_2.black_count == 0
    assert gc_2.call_store_method
    assert not gc_2.new_high_score
    assert not gc_2.game_ends

    board_3 = Board(8, 8, 100)
    gm_3 = GameManager(board_3)
    gc_3 = GameController(board_3, gm_3, 800, 800)
    assert gc_3.board == board_3
    assert gc_3.gm == gm_3
    assert gc_3.WIDTH == 800
    assert gc_3.HEIGHT == 800
    assert gc_3.black_count == 0
    assert gc_3.call_store_method
    assert not gc_3.new_high_score
    assert not gc_3.game_ends


def test_end_game():
    board = Board(8, 8, 100)
    gm = GameManager(board)
    gc = GameController(board, gm, 800, 800)

    gc.gm.no_player_moves = True
    gc.gm.no_ai_moves = False
    gc.end_game()
    assert not gc.game_ends

    gc.gm.no_player_moves = False
    gc.gm.no_ai_moves = True
    gc.end_game()
    assert not gc.game_ends

    gc.gm.no_player_moves = False
    gc.gm.no_ai_moves = False
    gc.end_game()
    assert not gc.game_ends


def test_compare_score():
    board = Board(8, 8, 100)
    gm = GameManager(board)
    gc = GameController(board, gm, 800, 800)

    gc.black_count = 20
    gc.compare_score("results_for_test.txt")
    assert gc.new_high_score

    gc.black_count = 3
    gc.new_high_score = False  # reset the boolean variable
    gc.compare_score("results_for_test.txt")
    assert not gc.new_high_score

    gc.black_count = 40
    gc.new_high_score = False  # reset the boolean variable
    gc.compare_score("results_for_test.txt")
    assert gc.new_high_score
