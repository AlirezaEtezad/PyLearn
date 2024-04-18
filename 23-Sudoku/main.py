import sys
import random
from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import *
from ui_main_window import Ui_MainWindow
from sudoku import Sudoku

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_openfile.triggered.connect(self.open_file)
        self.ui.menu_solve.triggered.connect(self.solve_game)
        self.ui.menu_help.triggered.connect(self.help)
        self.ui.menu_exit.triggered.connect(exit)
        self.ui.dark_mode.triggered.connect(self.enable_dark_mode)
        self.ui.light_mode.triggered.connect(self.enable_light_mode)
        self.ui.difficulty_easy.triggered.connect(self.difficulty_easy)
        self.ui.difficulty_normal.triggered.connect(self.difficulty_normal)
        self.ui.difficulty_hard.triggered.connect(self.difficulty_hard)
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        self.duplicate_cells = set()
        self.read_only_cells = set()
        self.dark_mode_stylesheet = "background-color: #333; color: #FFF;"
        self.light_mode_stylesheet = ""
        self.difficulty = 0.3
        self.new_game()
        
    def difficulty_easy(self):
        if self.difficulty == 0.3:
            return
        else:
            self.difficulty = 0.3
            self.new_game()
            print(f"changed to {self.difficulty}")


    def difficulty_normal(self):
        if self.difficulty == 0.5:
            return
        else:
            self.difficulty = 0.5
            self.new_game()
            print(f"changed to {self.difficulty}")

    def difficulty_hard(self):
        if self.difficulty == 0.6:
            return
        else:
            self.difficulty = 0.6
            self.new_game()
            print(f"changed to {self.difficulty}")


    def help(self):
        QMessageBox.information(self, "Help", "This is a Sudoku game. Fill the board with numbers 1-9 such that each row, column, and 3x3 subgrid contains all of the digits 1-9.")

    def close(self):
        exit(0)


    def enable_dark_mode(self):
        self.set_stylesheet(self.dark_mode_stylesheet)


    def enable_light_mode(self):
        self.set_stylesheet(self.light_mode_stylesheet)


    def set_stylesheet(self, stylesheet):
        self.setStyleSheet(stylesheet)
        for row in self.line_edits:
            for cell in row:
                cell.setStyleSheet(stylesheet)
        self.highlight_duplicate()




    def generate_board(self, puzzle_board):
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setReadOnly(False)
                new_cell.setStyleSheet("")  # doesnt work
                new_cell.setAlignment(Qt.AlignCenter)
                new_cell.setFixedSize(50, 50)

                if puzzle_board[i][j] not in [None, 0]:  # None or "0" returns True
                    new_cell.setText(str(puzzle_board[i][j]))
                    new_cell.setReadOnly(True)
                    new_cell.setStyleSheet("background-color: lightgrey")
                    self.read_only_cells.add((i, j))
                    
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell


    def new_game(self):
        game = random.randint(1, 1000)
        puzzle = Sudoku(3, seed=game).difficulty(self.difficulty)
        puzzle_board = puzzle.board
        self.generate_board(puzzle_board)
        self.solution = puzzle.solve().board

    def solve_game(self):
        puzzle_board = self.solution
        self.generate_board(puzzle_board)

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "Open file...")[0]
        if file_path:
            try:
                with open(file_path, "r") as f:
                    rows = f.read().split("\n")
                puzzle_board = [[int(cell) for cell in row.split()] for row in rows]
                self.generate_board(puzzle_board)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while opening the file: {str(e)}")


    def highlight_duplicate(self):
        style_sheet = "color: red"
        for i, j in self.duplicate_cells:
            current_style = self.line_edits[i][j].styleSheet()
            if current_style:
                new_style = current_style + ";" + style_sheet
            else:
                new_style = style_sheet
            self.line_edits[i][j].setStyleSheet(new_style)
        for i, j in self.read_only_cells:
            if (i, j) not in self.duplicate_cells:
                new_style = "background-color : lightgrey"
                self.line_edits[i][j].setStyleSheet(new_style)
        
        for i in range(9):
            for j in range(9):
                if (i, j ) not in self.read_only_cells:
                    if (i, j) not in self.duplicate_cells:
                        self.line_edits[i][j].setStyleSheet("")
    
    def check(self):
        self.duplicate_cells.clear()
        is_completed = True
        for i in range(9):
            for j in range(9):
                text = self.line_edits[i][j].text()
                if text and not "": # come back here again
                   # print(text)
                    for k in range(j+1, 9):
                    #    print(i,j,k)
                        if text == self.line_edits[i][k].text():
                            # self.highlight_duplicate(i, j)
                            # self.highlight_duplicate(i, k)
                            self.duplicate_cells.add((i, j))
                            self.duplicate_cells.add((i, k))   

        for j in range(9):
            for i in range(9):
                text = self.line_edits[i][j].text()
                if text and not "":
                    for k in range(i+1, 9):
                        if text == self.line_edits[k][j].text():
                            # self.highlight_duplicate(i, j)
                            # self.highlight_duplicate(k, j)
                            self.duplicate_cells.add((i, j))
                            self.duplicate_cells.add((k, j))

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        text = self.line_edits[row + i][col + j].text()
                        if text:
                            if text in seen:
                                for x in range(3):
                                    for y in range(3):
                                        if self.line_edits[row + x][col + y].text() == text:
                                            # self.highlight_duplicate(row + x, col + y)
                                            self.duplicate_cells.add((row + x, col + y))

                            else:
                                seen.add(text)

        self.highlight_duplicate()
       # print(self.duplicate_cells)
        if len(self.duplicate_cells) == 0:
            for i in range(9):
                for j in range(9):
                    if not self.line_edits[i][j].text():
                        is_completed = False
                        break
                if not is_completed:
                    break
            if is_completed:
                QMessageBox.information(self, "Congratulations!", "You've completed the Sudoku puzzle!")




        return False



    def validation(self, i, j, text):
        if text and text not in str(list(range(1, 10))):
            self.line_edits[i][j].setText("")
        else:
            self.line_edits[i][j].setStyleSheet("")
        self.check()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
