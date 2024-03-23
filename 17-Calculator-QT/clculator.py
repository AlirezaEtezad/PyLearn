
import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial


app = QApplication([])
loader = QUiLoader()
window = loader.load("main.ui")
window.show()


def num(x):
    num = window.box.text()  
    window.box.setText(num + x)


# def one():
#     num = window.box.text()  
#     window.box.setText(num + "1")
# def two():
#     num = window.box.text()  
#     window.box.setText(num + "2")
# def three():
#     num = window.box.text()  
#     window.box.setText(num + "3")    
# def four():
#     num = window.box.text()  
#     window.box.setText(num + "4") 
# def five():
#     num = window.box.text()  
#     window.box.setText(num + "5") 
# def six():
#     num = window.box.text()  
#     window.box.setText(num + "6") 
# def seven():
#     num = window.box.text()  
#     window.box.setText(num + "7") 
# def eight():
#     num = window.box.text()  
#     window.box.setText(num + "8") 
# def nine():
#     num = window.box.text()  
#     window.box.setText(num + "9") 
# def zero():
#     num = window.box.text()  
#     window.box.setText(num + "0") 
# def dot():
#     num = window.box.text()  
#     window.box.setText(num + ".") 


def clear():
    window.box.setText("")

def sum():
    global num1 , num2 , result
    global operator
    operator = "+"
    num1 = window.box.text()
    window.box.setText("")

def sub():
    global num1, num2 , result 
    global operator
    operator = str("-")
    num1 = window.box.text()
    window.box.setText("")

def mult():
    global num1, num2 , result 
    global operator
    operator = "x"
    num1 = window.box.text()
    window.box.setText("")
    
def div():
    global num1, num2 , result
    global operator
    operator = "÷"
    num1 = window.box.text()
    window.box.setText("")

def sin():
    global num1, result
    global operator
    operator = "sin"
    num1 = window.box.text()
    result = math.sin(math.radians(float(num1)))
    window.box.setText(str(result))

def cos():
    global num1, result
    global operator
    operator = "cos"
    num1 = window.box.text()
    result = math.cos(math.radians(float(num1)))
    window.box.setText(str(result))

def tan():
    global num1, result
    global operator
    operator = "tan"
    num1 = window.box.text()
    result = math.tan(math.radians(float(num1)))
    window.box.setText(str(result))

def cot():
    global num1, result
    global operator
    operator = "cot"
    num1 = window.box.text()
    if math.tan(math.radians(float(num1)))==0:
        window.box.setText("ERROR")
    else:
        result = 1/math.tan(math.radians(float(num1)))
        window.box.setText(str(result))

def log():
    global num1, result
    global operator
    operator = "log"
    num1 = window.box.text()
    if float(num1)>0:
        result = math.log(int(num1))
        window.box.setText(str(result))
    else:
        window.box.setText("ERROR")

def percent():
    global num1, num2 , result 
    global operator
    operator = "x"
    num1 = float(window.box.text()) / 100
    window.box.setText("")

def sqrt():
    global num1, result
    global operator
    operator= "√"
    num1 = window.box.text()
    if float(num1)<0:
        window.box.setText("ERROR")
    else:
        result = math.sqrt(float(num1))
        window.box.setText(str(result))



def calculate(result):
        if operator == "-" :
            num2 = window.box.text()
            result = float(num1) - float(num2)
            window.box.setText(str(result))
        
        elif operator == "+" :
            num2 = window.box.text()
            result = float(num1) + float(num2)
            window.box.setText(str(result))
        
        elif operator == "x" :
            num2 = window.box.text()
            result = float(num1) * float(num2)
            window.box.setText(str(result))

        elif operator == "÷" :
            num2 = window.box.text()
            if num2 == 0 :
                window.box.setText("ERROR")            
            else:
                result = float(num1) / float(num2)
                window.box.setText(str(result)) 


window.btn_1.clicked.connect(partial(num, "1"))
window.btn_2.clicked.connect(partial(num, "2"))
window.btn_3.clicked.connect(partial(num, "3"))
window.btn_4.clicked.connect(partial(num, "4"))
window.btn_5.clicked.connect(partial(num, "5"))
window.btn_6.clicked.connect(partial(num, "6"))
window.btn_7.clicked.connect(partial(num, "7"))
window.btn_8.clicked.connect(partial(num, "8"))
window.btn_9.clicked.connect(partial(num, "9"))
window.btn_0.clicked.connect(partial(num, "0"))
window.btn_dot.clicked.connect(partial(num, "."))

window.btn_clear.clicked.connect(clear)

window.btn_sum.clicked.connect(sum)
window.btn_sub.clicked.connect(sub)
window.btn_mult.clicked.connect(mult)
window.btn_div.clicked.connect(div)

window.btn_sin.clicked.connect(sin)
window.btn_cos.clicked.connect(cos)
window.btn_tan.clicked.connect(tan)
window.btn_cot.clicked.connect(cot)
window.btn_log.clicked.connect(log)
window.btn_percent.clicked.connect(percent)
window.btn_sqrt.clicked.connect(sqrt)

window.btn_equal.clicked.connect(calculate)


app.exec()