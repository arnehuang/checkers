from copy import deepcopy


class Board:
    RED_PIECE = "red"
    BLACK_PIECE = "black"
    RED_KING = "red_king"
    BLACK_KING = "black_king"
    EMPTY = "empty"
    INITAL_BOARD_STATE = [
        ["board", "a", "b", "c", "d", "e", "f", "g", "h"],
        ["1", EMPTY, RED_PIECE, EMPTY, RED_PIECE, EMPTY, RED_PIECE, EMPTY, RED_PIECE],
        ["2", RED_PIECE, EMPTY, RED_PIECE, EMPTY, RED_PIECE, EMPTY, RED_PIECE, EMPTY],
        ["3", EMPTY, RED_PIECE, EMPTY, RED_PIECE, EMPTY, RED_PIECE, EMPTY, RED_PIECE],
        ["4", EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        ["5", EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        ["6", BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY],
        ["7", EMPTY, BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY, BLACK_PIECE],
        ["8", BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY, BLACK_PIECE, EMPTY]
    ]

    def __init__(self):
        self.state = deepcopy(Board.INITAL_BOARD_STATE)
        self.turn = deepcopy(Board.RED_PIECE)

    def __str__(self):
        return self.state.__str__()

    def __repr__(self):
        return self.state.__repr__()

    def print_state(self):
        print(*self.state, sep="\n")

    def execute_move(self, instructions):
        # INSTRUCTIONS_FORMAT = "A1 to B1"
        from_instructions = instructions[:2]
        to_instructions = instructions[-2:]
        self._validate_move(from_instructions, to_instructions)
        self._record_move(from_instructions, to_instructions)
        self._iterate_turn()

    def check_for_win(self):
        return True

    def _get_coordinates(self, coordinates):
        x_coord = int(ord(coordinates[0]) - 96)
        y_coord = int(coordinates[1])
        return self.state[y_coord][x_coord]

    def _is_diagonal(self, coordinate1, coordinate2, forward_only=True, hop=False):
        distance = 1
        if hop:
            distance = 2
        x_coord1 = int(ord(coordinate1[0]) - 96)
        y_coord1 = int(coordinate1[1])
        x_coord2 = int(ord(coordinate2[0]) - 96)
        y_coord2 = int(coordinate2[1])
        if forward_only:
            if self.turn == Board.RED_PIECE:
                return (x_coord1 == (x_coord2 + distance) or x_coord1 == (x_coord2 - distance)) \
                       and y_coord1 == (y_coord2 - distance)
            else:
                return (x_coord1 == (x_coord2 + distance) or x_coord1 == (x_coord2 - distance)) \
                       and y_coord1 == (y_coord2 + distance)
        else:
            return (x_coord1 == (x_coord2 + distance) or x_coord1 == (x_coord2 - distance)) and (
                    y_coord1 == (y_coord2 - distance) or y_coord1 == (y_coord2 + distance))

    def _is_valid_hop(self, coordinate1, coordinate2, piece_to_move):
        forward_only = True
        distance = 2
        if piece_to_move in [Board.RED_KING, Board.BLACK_KING]:
            forward_only = False
        x_coord1 = int(ord(coordinate1[0]) - 96)
        y_coord1 = int(coordinate1[1])
        x_coord2 = int(ord(coordinate2[0]) - 96)
        y_coord2 = int(coordinate2[1])

        # check kings moving to valid destination first
        valid_destination = (x_coord1 == (x_coord2 + distance) or x_coord1 == (x_coord2 - distance)) and (
                y_coord1 == (y_coord2 - distance) or y_coord1 == (y_coord2 + distance))
        if forward_only:
            if self.turn == Board.RED_PIECE:
                valid_destination = (x_coord1 == (x_coord2 + distance) or x_coord1 == (x_coord2 - distance)) \
                                    and y_coord1 == (y_coord2 - distance)
            else:
                valid_destination = (x_coord1 == (x_coord2 + distance) or x_coord1 == (x_coord2 - distance)) \
                                    and y_coord1 == (y_coord2 + distance)
        if not valid_destination:
            return False

        middle_coord_x = x_coord1 - 1
        middle_coord_y = y_coord1 - 1
        if x_coord1 == (x_coord2 - distance):
            middle_coord_x = x_coord1 + 1
        if y_coord1 == (y_coord2 - distance):
            middle_coord_y = y_coord1 + 1
        middle_piece = self.state[middle_coord_y][middle_coord_x]
        if self.turn == Board.RED_PIECE:
            if middle_piece in [Board.BLACK_PIECE, Board.BLACK_KING]:
                return True
        else:
            if middle_piece in [Board.RED_PIECE, Board.RED_KING]:
                return True
        return False

    def _validate_move(self, from_instructions, to_instructions):
        piece_to_move = self._get_coordinates(from_instructions)
        # Empty Piece
        if piece_to_move == Board.EMPTY:
            raise ValueError(f"Illegal move: {from_instructions} is an empty square")
        # Not your turn
        if (self.turn == Board.RED_PIECE and (piece_to_move not in [Board.RED_PIECE, Board.RED_KING])) or (
                self.turn == Board.BLACK_PIECE and (piece_to_move not in [Board.BLACK_PIECE, Board.BLACK_KING])):
            raise ValueError(f"Illegal move: {from_instructions} is {piece_to_move}, but it's {self.turn}'s turn")
        destination = self._get_coordinates(to_instructions)
        if destination != Board.EMPTY:
            raise ValueError(f"Illegal move: {to_instructions} is {destination}, which is not empty")

        # moving naturally /  taking pieces
        can_move_diagonally_forward = self._is_diagonal(from_instructions, to_instructions, forward_only=True)
        can_move_diagonally_king = (piece_to_move == Board.RED_KING or piece_to_move == Board.BLACK_KING) \
                                   and self._is_diagonal(from_instructions, to_instructions, forward_only=False)
        can_hop = self._is_valid_hop(from_instructions, to_instructions, piece_to_move)
        if (not can_move_diagonally_forward) and (not can_move_diagonally_king) and (not can_hop):
            raise ValueError(f"Illegal move: {from_instructions} to {to_instructions} is not a valid move")

        # TODO: Implement Forced to take

    def _record_move(self, from_instructions, to_instructions):
        piece_to_move = self._get_coordinates(from_instructions)
        can_hop = self._is_valid_hop(from_instructions, to_instructions, piece_to_move)
        from_x_coord = int(ord(from_instructions[0]) - 96)
        from_y_coord = int(from_instructions[1])
        to_x_coord = int(ord(to_instructions[0]) - 96)
        to_y_coord = int(to_instructions[1])
        piece_to_set = piece_to_move
        if self.turn == Board.RED_PIECE and to_y_coord == 8 and piece_to_move == Board.RED_PIECE:
            piece_to_set = Board.RED_KING
        elif self.turn == Board.BLACK_PIECE and to_y_coord == 1 and piece_to_move == Board.BLACK_PIECE:
            piece_to_set = Board.BLACK_KING
        self.state[from_y_coord][from_x_coord] = Board.EMPTY
        self.state[to_y_coord][to_x_coord] = piece_to_set
        if can_hop:
            distance = 2
            middle_coord_x = from_x_coord - 1
            middle_coord_y = from_y_coord - 1
            if from_x_coord == (to_x_coord - distance):
                middle_coord_x = from_x_coord + 1
            if from_y_coord == (to_y_coord - distance):
                middle_coord_y = from_y_coord + 1
            self.state[middle_coord_y][middle_coord_x] = Board.EMPTY

    def _iterate_turn(self):
        if self.turn == Board.RED_PIECE:
            self.turn = Board.BLACK_PIECE
        else:
            self.turn = Board.RED_PIECE
