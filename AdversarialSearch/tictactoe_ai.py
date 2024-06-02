from minmax import find_best_move
from tictactoe import TTTBoard
from board import Move, Board


def main():
    board: Board = TTTBoard()
    while True:
        print(board)
        human_move = get_player_move(board)
        board = board.move(human_move)
        print(board)
        if board.is_win:
            print("You win!")
            break
        elif board.is_draw:
            print("It's a draw!")
            break
        computer_move = find_best_move(board)
        print(f"Computer move is {computer_move}")
        board = board.move(computer_move)
        print(board)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("It's a draw!")
            break


def get_player_move(board: Board):
    player_move: Move = Move(-1)
    while player_move not in board.get_legal_moves:
        print("Enter your move as a number between 0 and 8")
        move = int(input())
        player_move = Move(move)
    return player_move


if __name__ == "__main__":
    main()
