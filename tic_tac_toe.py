import random

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, player):
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    for a, b, c in combos:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    return all(space != " " for space in board)


def player_move(board):
    while True:
        try:
            move = int(input("Выберите позицию (1-9): ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Позиция занята или выходит за пределы доски.")
        except (ValueError, IndexError):
            print("Некорректный ввод, попробуйте ещё раз.")


def computer_move(board):
    # check winning move
    for move in range(9):
        if board[move] == " ":
            board[move] = "O"
            if check_winner(board, "O"):
                return
            board[move] = " "
    # block opponent winning move
    for move in range(9):
        if board[move] == " ":
            board[move] = "X"
            if check_winner(board, "X"):
                board[move] = "O"
                return
            board[move] = " "
    available = [i for i, space in enumerate(board) if space == " "]
    if available:
        board[random.choice(available)] = "O"


def main():
    board = [" "] * 9
    print("Добро пожаловать в Крестики-нолики!")
    print_board(board)
    while True:
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Вы победили!")
            break
        if is_draw(board):
            print("Ничья!")
            break
        computer_move(board)
        print("Ход компьютера:")
        print_board(board)
        if check_winner(board, "O"):
            print("Компьютер победил.")
            break
        if is_draw(board):
            print("Ничья!")
            break


if __name__ == "__main__":
    main()
