from board import Board

if __name__ == "__main__":
    board = Board()
    while True:

        print("The current game state is:")
        board.print_state()
        inp = input(f"It's {board.turn}'s turn. What's the next move? e.g. a1 to b3 ")
        try:
            board.execute_move(inp)
        except Exception as E:
            print(f"Unable to process that move. Error:")
            print(E)