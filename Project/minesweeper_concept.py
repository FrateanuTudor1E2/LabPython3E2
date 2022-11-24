import random
def create_board_variable_size(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(0)
    return board
def put_mines(board, mines):
    for i in range(mines):
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
        board[x][y] = -1
    return board
def put_numbers(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == -1:
                continue
            else:
                board[i][j] = count_mines(board, i, j)
    return board
def count_mines(board, x, y):
    mines = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i < 0 or y + j < 0 or x + i >= len(board) or y + j >= len(board):
                continue
            else:
                if board[x + i][y + j] == -1:
                    mines += 1
    return mines
def make_graphics(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == -1:
                print('X', end=' ')
            else:
                print(board[i][j], end=' ')
        print()

def main():
    board = create_board_variable_size(10)
    board = put_mines(board, 10)
    board = put_numbers(board)
    make_graphics(board)
if __name__ == "__main__":
    main()
