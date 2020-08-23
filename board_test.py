from board import Board


def test_constructor():
    board_1 = Board(2, 2, 100)
    assert board_1.ROWS == 2
    assert board_1.COLUMNS == 2
    assert board_1.SPACING == 100
    assert board_1.spaces[0][0].color == 255
    assert board_1.spaces[1][1].color == 255
    assert board_1.spaces[0][1].color == 0
    assert board_1.spaces[1][0].color == 0

    board_2 = Board(4, 4, 100)
    assert board_2.ROWS == 4
    assert board_2.COLUMNS == 4
    assert board_2.SPACING == 100
    assert board_2.spaces[1][1].color == 255
    assert board_2.spaces[2][2].color == 255
    assert board_2.spaces[2][1].color == 0
    assert board_2.spaces[1][2].color == 0
    assert board_2.spaces[0][0] is None
    assert board_2.spaces[3][3] is None

    board_3 = Board(8, 8, 100)
    assert board_3.ROWS == 8
    assert board_3.COLUMNS == 8
    assert board_3.SPACING == 100
    assert board_3.spaces[3][3].color == 255
    assert board_3.spaces[4][4].color == 255
    assert board_3.spaces[4][3].color == 0
    assert board_3.spaces[3][4].color == 0
    assert board_3.spaces[0][0] is None
    assert board_3.spaces[7][7] is None
