import turtle

line = turtle.Pen()
length = 30
for i in range(3, 11):
    angle = 360 - (360 // i)
    length += 10
    line.penup()
#    line.right(30)
#    line.forward(10)
    line.pendown()
    for j in range(i):
        line.forward(length)
        line.right(angle)
