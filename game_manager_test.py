from game_manager import GameManager
from board import Board


def test_constructor():
    board_1 = Board(2, 2, 100)
    gm_1 = GameManager(board_1)
    assert gm_1.turn
    assert gm_1.board == board_1
    assert not gm_1.no_ai_moves
    assert not gm_1.no_player_moves
    assert gm_1.directions == [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
                               (-1, -1), (-1, 0), (-1, 1)]
    assert gm_1.legal_move == dict()

    board_2 = Board(4, 4, 50)
    gm_2 = GameManager(board_2)
    assert gm_2.turn
    assert gm_2.board == board_2
    assert not gm_2.no_ai_moves
    assert not gm_2.no_player_moves
    assert gm_2.directions == [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
                               (-1, -1), (-1, 0), (-1, 1)]
    assert gm_2.legal_move == dict()

    board_3 = Board(8, 8, 100)
    gm_3 = GameManager(board_3)
    assert gm_3.turn
    assert gm_3.board == board_3
    assert not gm_3.no_ai_moves
    assert not gm_3.no_player_moves
    assert gm_3.directions == [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
                               (-1, -1), (-1, 0), (-1, 1)]
    assert gm_3.legal_move == dict()


def test_player_make_move():
    board_1 = Board(4, 4, 100)
    gm_1 = GameManager(board_1)
    gm_1.player_make_move(10, 100)
    assert gm_1.legal_move == {(0, 1): [(1, 1)], (1, 0): [(1, 1)],
                               (2, 3): [(2, 2)], (3, 2): [(2, 2)]}
    assert gm_1.board.spaces[0][1].color == 0

    board_2 = Board(8, 8, 100)
    gm_2 = GameManager(board_2)
    gm_2.player_make_move(10, 10)
    assert gm_2.legal_move == {(5, 4): [(4, 4)], (2, 3): [(3, 3)],
                               (4, 5): [(4, 4)], (3, 2): [(3, 3)]}
    assert not gm_2.board.spaces[0][0]

    board_3 = Board(6, 6, 100)
    gm_3 = GameManager(board_3)
    gm_3.player_make_move(400, 300)
    assert gm_3.legal_move == {(1, 2): [(2, 2)], (4, 3): [(3, 3)],
                               (3, 4): [(3, 3)], (2, 1): [(2, 2)]}
    assert gm_3.board.spaces[4][3].color == 0


def test_player_make_move():
    board_1 = Board(4, 4, 100)
    gm_1 = GameManager(board_1)
    gm_1.ai_make_move()
    assert gm_1.legal_move == {(0, 2): [(1, 2)], (1, 3): [(1, 2)],
                               (2, 0): [(2, 1)], (3, 1): [(2, 1)]}

    board_2 = Board(8, 8, 100)
    gm_2 = GameManager(board_2)
    gm_2.ai_make_move()
    assert gm_2.legal_move == {(2, 4): [(3, 4)], (3, 5): [(3, 4)],
                               (4, 2): [(4, 3)], (5, 3): [(4, 3)]}

    board_3 = Board(6, 6, 100)
    gm_3 = GameManager(board_3)
    gm_3.ai_make_move()
    assert gm_3.legal_move == {(1, 3): [(2, 3)], (2, 4): [(2, 3)],
                               (3, 1): [(3, 2)], (4, 2): [(3, 2)]}


def test_find_move():
    board = Board(8, 8, 100)
    gm = GameManager(board)

    gm.find_moves(gm.board.spaces[3][4], 255)
    assert gm.legal_move == {(5, 4): [(4, 4)], (3, 2): [(3, 3)]}

    gm.find_moves(gm.board.spaces[4][3], 255)
    assert gm.legal_move == {(5, 4): [(4, 4)], (2, 3): [(3, 3)],
                             (4, 5): [(4, 4)], (3, 2): [(3, 3)]}

    # reset the dictionary to empty
    gm.legal_move = dict()

    gm.find_moves(gm.board.spaces[3][3], 0)
    assert gm.legal_move == {(3, 5): [(3, 4)], (5, 3): [(4, 3)]}

    gm.find_moves(gm.board.spaces[4][4], 0)
    assert gm.legal_move == {(3, 5): [(3, 4)], (5, 3): [(4, 3)],
                             (4, 2): [(4, 3)], (2, 4): [(3, 4)]}


def test_on_board():
    board = Board(8, 8, 100)
    gm = GameManager(board)
    assert gm.on_board((1, 1))
    assert not gm.on_board((8, 7))
    assert gm.on_board((0, 0))
    assert not gm.on_board((9, 10))


def test_flip():
    board = Board(8, 8, 100)
    gm = GameManager(board)

    gm.flip([(3, 4)], 255)
    assert gm.board.spaces[3][4].color == 255

    gm.flip([(4, 3)], 17)
    assert gm.board.spaces[4][3].color == 17

    gm.flip([(3, 3), (4, 4)], 70)
    assert gm.board.spaces[3][3].color == 70
    assert gm.board.spaces[4][4].color == 70


def test_smart_ai():
    board = Board(8, 8, 100)
    gm = GameManager(board)

    assert gm.smart_ai({(2, 4): [(3, 4), (4, 4)], (3, 6): [(4, 5)]}) == (2, 4)
    assert gm.smart_ai({(4, 6): [(4, 5), (4, 4)], (2, 5): [(3, 4)]}) == (4, 6)
    assert gm.smart_ai({(3, 7): [(0, 0), (1, 2), (3, 4)], 
                        (4, 6): [(4, 5), (4, 4)], (2, 5): [(3, 4)]}) == (3, 7)
