import unittest

from board import Board


class TestBoard(unittest.TestCase):
    maxDiff = None

    def test_construct_board(self):
        board = Board()
        assert board.state == Board.INITAL_BOARD_STATE
        board.print_state()

    def test_validate_move_illegal_moves(self):
        board = Board()
        # illegal move due to trying to move empty square
        self.assertRaises(ValueError, board.execute_move, "a1 to a2")
        # illegal move due to not your turn
        self.assertRaises(ValueError, board.execute_move, "a6 to b5")
        # illegal move due to trying to not move diagonally
        self.assertRaises(ValueError, board.execute_move, "b3 to b4")
        # illegal move due to trying to hop over own piece
        self.assertRaises(ValueError, board.execute_move, "c2 to a4")

    def test_acceptable_move(self):
        board = Board()
        # acceptable move
        self.assertIsNone(board.execute_move("b3 to a4"))

    def test_record_move(self):
        # test state changes correctly
        board = Board()
        board.execute_move("b3 to a4")
        EXPECTED_STATE = [
            ["board", "a", "b", "c", "d", "e", "f", "g", "h"],
            ["1", Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE],
            ["2", Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE, Board.EMPTY],
            ["3", Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE],
            ["4", Board.RED_PIECE, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY,
             Board.EMPTY],
            ["5", Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY,
             Board.EMPTY],
            ["6", Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY,
             Board.BLACK_PIECE, Board.EMPTY],
            ["7", Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE,
             Board.EMPTY, Board.BLACK_PIECE],
            ["8", Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY,
             Board.BLACK_PIECE, Board.EMPTY]
        ]
        self.assertListEqual(board.state, EXPECTED_STATE)
        return

    def test_record_move_take(self):
        # test state changes correctly
        board = Board()
        board.execute_move("b3 to a4")
        board.execute_move("c6 to b5")
        board.execute_move("a4 to c6")
        EXPECTED_STATE = [
            ["board", "a", "b", "c", "d", "e", "f", "g", "h"],
            ["1", Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE],
            ["2", Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE, Board.EMPTY],
            ["3", Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE],
            ["4", Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY,
             Board.EMPTY],
            ["5", Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY,
             Board.EMPTY],
            ["6", Board.BLACK_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY,
             Board.BLACK_PIECE, Board.EMPTY],
            ["7", Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE,
             Board.EMPTY, Board.BLACK_PIECE],
            ["8", Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY,
             Board.BLACK_PIECE, Board.EMPTY]
        ]
        self.assertListEqual(board.state, EXPECTED_STATE)
        return

    def test_record_move_take_black(self):
        # test state changes correctly
        board = Board()
        board.execute_move("b3 to a4")
        board.execute_move("g6 to h5")
        board.execute_move("a4 to b5")
        board.execute_move("c6 to a4")
        board.print_state()
        EXPECTED_STATE = [
            ["board", "a", "b", "c", "d", "e", "f", "g", "h"],
            ["1", Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE],
            ["2", Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE, Board.EMPTY],
            ["3", Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.RED_PIECE, Board.EMPTY, Board.RED_PIECE, Board.EMPTY,
             Board.RED_PIECE],
            ["4", Board.BLACK_PIECE, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY,
             Board.EMPTY],
            ["5", Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.EMPTY,
             Board.BLACK_PIECE],
            ["6", Board.BLACK_PIECE, Board.EMPTY, Board.EMPTY, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY,
             Board.EMPTY, Board.EMPTY],
            ["7", Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE,
             Board.EMPTY, Board.BLACK_PIECE],
            ["8", Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY, Board.BLACK_PIECE, Board.EMPTY,
             Board.BLACK_PIECE, Board.EMPTY]
        ]
        self.assertListEqual(board.state, EXPECTED_STATE)
        return

    def test_check_for_win(self):
        # non winning state
        assert True
        # winning state
        assert True
