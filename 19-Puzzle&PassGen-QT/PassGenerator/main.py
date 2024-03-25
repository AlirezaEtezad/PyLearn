import random
import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QLCDNumber, QRadioButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication(sys.argv)
loader = QUiLoader()
main_window = loader.load("main_window.ui")
main_window.show()



alphabets_small = list(range(ord("a"), ord("z")+1))
alphabets_capital = list(range(ord("A"), ord("Z")+1))
numbers = list(range(0, 10))
signs = ["!","@","#","$","%","^","&","*",]


# print (alphabets_small)
# print (alphabets_capital)
# print (numbers)
# print (signs)
# print(chr)

def choose_complexity():
    global complexity
    if main_window.rdbtn_simple.isChecked():
        complexity = 1
    elif main_window.rdbtn_normal.isChecked():
        complexity = 2
    elif main_window.rdbtn_strong.isChecked():
        complexity = 3




def choose_char():
    choose = random.randint(1,4)
   # print (choose)
    if choose == 1:
        chosen = random.choice(alphabets_small)
        char = chr(chosen)
    elif choose == 2:
        chosen = random.choice(alphabets_capital)
        char = chr(chosen)
    elif choose == 3:
        char = str(random.choice(numbers))
    else:
        char = random.choice(signs)
    return char




def generate_pass():
    global simple_pass, normal_pass, strong_pass
    a = choose_char()
    b = choose_char()
    c = choose_char()
    d = choose_char()
    e = choose_char()
    f = choose_char()
    g = choose_char()
    h = choose_char()
    i = choose_char()
    j = choose_char()
    k = choose_char()
    l = choose_char()
    m = choose_char()
    n = choose_char()
    o = choose_char()
    simple_pass = a + b + c + d + f + g
    normal_pass = simple_pass + h + i + j + k
    strong_pass = normal_pass + l + m + n + o
    show_pass()

def show_pass():
    if complexity == 1:
        generated_pass = simple_pass

    elif complexity == 2:
        generated_pass = normal_pass
    else:
        generated_pass = strong_pass

    main_window.txt_box.setText(generated_pass)




rdbtn_simple = main_window.findChild(QRadioButton, "rdbtn_simple")
rdbtn_normal = main_window.findChild(QRadioButton, "rdbtn_normal")
rdbtn_strong = main_window.findChild(QRadioButton, "rdbtn_strong")
rdbtn_simple.toggled.connect(choose_complexity)
rdbtn_normal.toggled.connect(choose_complexity)
rdbtn_strong.toggled.connect(choose_complexity)

main_window.btn_generate.clicked.connect(generate_pass)


app.exec()