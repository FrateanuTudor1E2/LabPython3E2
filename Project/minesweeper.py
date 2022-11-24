import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui
from PyQt5.uic.properties import QtCore
from fontTools.merge import layout

import minesweeper_concept as ms

def make_minesweeper_board():
    board = ms.create_board_variable_size(30)
    board = ms.put_mines(board, 30)
    board = ms.put_numbers(board)
    return board


def make_window_with_board_tiles(board):
    app = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    window.setWindowTitle('Minesweeper')
    window.resize(1000, 800)
    layout = QtWidgets.QGridLayout()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == -1:
                tile = QtWidgets.QLabel()
                tile.setPixmap(QtGui.QPixmap('mine.png'))
                layout.addWidget(tile, i, j)
            else:
                tile = QtWidgets.QLabel()
                tile.setText(str(board[i][j]))
                layout.addWidget(tile, i, j)

    window.setLayout(layout)
    window.show()
    app.exec_()

def make_buttons_on_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            button = QtWidgets.QPushButton()
            button.setText(str(board[i][j]))
            layout.addWidget(button, i, j)
def edit_minepng():
        from PIL import Image
        im = Image.open('mine.png')
        im = im.resize((50, 40))
        im.save('mine.png')
def main():
    edit_minepng()
    board = make_minesweeper_board()
    make_window_with_board_tiles(board)
    make_buttons_on_board(board)
if __name__ == "__main__":
    main()




