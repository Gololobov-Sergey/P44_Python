import random

size = 3
# board = [['X', ' ', '0'],['0', ' ', ' '],['X', '0', '0']]
board = [[f"{(i+j*size) + 1}" for i in range(size)] for j in range(size)]


def print_board(board):
    size = len(board)
    for i in range(size):
        for j in range(size):
            print(f"{board[i][j].center(3)}", end='')
            if j != size-1:
                print("|", end='')
        print()
        if i != size-1:
            print("---|"*(size-1), end='')
            print("---")


def move(board, num, symbol):
    size = len(board)
    board[(num-1) // size][(num-1) % size] = symbol

def get_free_cell(board):
    size = len(board)
    while True:
        num = random.randint(1, size**2)
        if board[(num-1) // size][(num-1) % size] != 'X' and board[(num-1) // size][(num-1) % size] != '0':
            return num

def input_number(board):
    return int(input("Виберіть номер : "))

def winner(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    if board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return " "



list_move = [input_number, get_free_cell]
move_symbol = ['X', '0']

for i in range(size**2):
    move(board, list_move[i%2](board), move_symbol[i%2])
    print_board(board)

