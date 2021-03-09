from Board import Board
from Piece import Piece
import math

from unittest.mock import MagicMock

def test_ctor_ok():
    board = Board(8)
    assert board.n == 8
    assert board.pieces == set()

def test_ctor_negative_number_error():
    board = Board(-1000)
    # TODO: assert that there is an exception being thrown

def test_ctor_infinity_error():
    board = Board(math.inf)
    # TODO: assert that there is an exception being thrown


def test_size_ok8():
     board = Board(8)
     assert board.size() == 8

def test_size_ok1000():
     board = Board(1000)
     assert board.size() == 1000

# @parametrized(1,3,8,1000)
# def test_size_ok(i):
#     board = Board(i)
#     assert board.size() == i

# @parametrized(-1000, -Infinity, Infinity, i, NaN, 0)
# def test_size_error(i):
#     board = Board(i)
#     # assert exception


def test_add_ok():
    board = Board(3)
    piece = Piece()

    board.add(piece)

    assert len(board.pieces) == 1
    assert piece in board.pieces

def test_adminissiblePlacementFor_true():
    board = Board(3)
    piece1 = Piece()
    piece1.attacks = MagicMock(return_value=False)
    board.add(piece1)

    piece2 = Piece()
    piece2.attacks = MagicMock(return_value=False)
    actual = board.admissiblePlacementFor(piece2)

    expected = True

    assert actual == expected

def test_adminissiblePlacementFor_false1():
    board = Board(3)
    piece1 = Piece()
    piece1.attacks = MagicMock(return_value=True)
    board.add(piece1)

    piece2 = Piece()
    piece2.attacks = MagicMock(return_value=False)
    actual = board.admissiblePlacementFor(piece2)

    expected = False

    assert actual == expected

def test_adminissiblePlacementFor_false2():
    board = Board(3)
    piece1 = Piece()
    piece1.attacks = MagicMock(return_value=False)
    board.add(piece1)

    piece2 = Piece()
    piece2.attacks = MagicMock(return_value=True)
    actual = board.admissiblePlacementFor(piece2)

    expected = False

    assert actual == expected

def test_adminissiblePlacementFor_false3():
    board = Board(3)
    piece1 = Piece()
    piece1.attacks = MagicMock(return_value=True)
    board.add(piece1)

    piece2 = Piece()
    piece2.attacks = MagicMock(return_value=True)
    actual = board.admissiblePlacementFor(piece2)

    expected = False

    assert actual == expected