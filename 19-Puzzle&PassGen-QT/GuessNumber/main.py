import random
import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QLCDNumber
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt


QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication(sys.argv)
loader = QUiLoader()
main_window = loader.load("main_window.ui")
main_window.show()

lcd = main_window.findChild(QLCDNumber, "lcd")


computer_number = random.randint(1,100)
count = 0

def update_lcd_value(new_value):
    lcd.display(new_value)


def play():
    global count
    user_number = int(main_window.txt_box.text())

    if computer_number == user_number :
        msg_box = QMessageBox(text= "You won!")
        msg_box.exec()
    elif computer_number > user_number:
        msg_box = QMessageBox(text= "Go Up")
        msg_box.exec()
    else:
        msg_box = QMessageBox(text= "Go Down")
        msg_box.exec()

    count +=1
    update_lcd_value(count)






main_window.btn_guess.clicked.connect(play)



app.exec()