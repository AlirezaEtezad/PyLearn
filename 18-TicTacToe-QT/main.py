import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QLCDNumber, QRadioButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication(sys.argv)
#app = QApplication([])

loader = QUiLoader()
main_window = loader.load("main_window.ui")
main_window.show()

player = "X"
win_count_X = 0
win_count_O = 0
game_mode = 1

lcd_X = main_window.findChild(QLCDNumber, "lcd_X")
lcd_O = main_window.findChild(QLCDNumber, "lcd_O")



def set_game_mode():
    global game_mode
    if main_window.one_player.isChecked():
        game_mode = 1
    else:
        game_mode = 2
    print(game_mode)


def new_game():
    for i in range (3):
        for j in range (3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("")


def reset():
    new_game()
    global win_count_O, win_count_X
    win_count_X = 0
    win_count_O = 0
    update_lcd_value_X(win_count_X)
    update_lcd_value_O(win_count_O)

def update_lcd_value_X(new_value):
    lcd_X.display(new_value)

def update_lcd_value_O(new_value):
    lcd_O.display(new_value)


def check_game():
    global winner, win_count_X, win_count_O 
    winner = None
    if buttons[0][0].text() == buttons[1][1].text() == buttons[2][2].text() != "":
        winner = buttons[0][0].text()
    elif buttons[0][2].text() == buttons[1][1].text() == buttons[2][0].text() != "":
        winner = buttons[0][2].text()
    
    for i in range(3):
        if buttons[i][0].text() == buttons[i][1].text() == buttons[i][2].text() !="":       
            winner = buttons[i][0].text()
            break    
    for j in range(3):
        if buttons[0][j].text() == buttons[1][j].text() == buttons[2][j].text() !="":
            winner = buttons[0][j].text()
            break
    
    if not winner:
        for i in range(3):
            for j in range(3):
                if buttons[i][j].text() == "":
                    return
    
        winner = "Nobody"

    if winner:    
        msg_box = QMessageBox(text= f"The Winner is {winner}")
        msg_box.exec()
        new_game()

        if winner == "X":
            win_count_X += 1
            update_lcd_value_X(win_count_X)
        elif winner == "O":
            win_count_O += 1
            update_lcd_value_O(win_count_O)
            
        # for i in range(3):
        #     for j in range(3):
        #         buttons[i][j].setEnabled(False)


def ai_play():
    # global player
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j].text() == ""]
    if empty_cells:
        chosen_cell = random.choice(empty_cells)
        buttons[chosen_cell[0]][chosen_cell[1]].setText("O")
        buttons[chosen_cell[0]][chosen_cell[1]].setStyleSheet("color: blue; background-color: Lightblue")
        # player = "X"
      #  check_game()


def play(row, col):
    global player
    # global buttons
    if buttons[row][col].text() == "":
        if player == "X":
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color: red; background-color: pink")
            player = "O"
            if game_mode == 1:
                ai_play()
                player = "X"


        elif player == "O" and game_mode ==2:
            buttons[row][col].setText("O")
            buttons[row][col].setStyleSheet("color: blue; background-color: Lightblue")
            player = "X"

        # if player == "O" and game_mode ==1:
        #     ai_play()


                # random.ra
        check_game()
        # print(empty_cells)




buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9],]



for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

main_window.btn_reset.clicked.connect(reset)


one_player = main_window.findChild(QRadioButton, "one_player")
#two_player = main_window.findChild(QRadioButton, "two_player")

one_player.toggled.connect(set_game_mode)
#two_player.toggled.connect(set_game_mode)



app.exec()