from minmax import find_best_move
from connectfour import C4Board
from board import Move, Board


def main():
    board: Board = C4Board()
    while True:
        # human_move: Move = get_player_move(board)
        human_move: Move = find_best_move(board, 4)
        board = board.move(human_move)
        if board.is_win:
            print("Human wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
        computer_move: Move = find_best_move(board, 3)
        print(f"Computer move is {computer_move}")
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break


def get_player_move(board) -> Move:
    player_move: Move = Move(-1)
    while player_move not in board.get_legal_moves:
        play: int = int(input("Enter a legal column (0-6):"))
        player_move = Move(play)
    return player_move


if __name__ == "__main__":
    main()
