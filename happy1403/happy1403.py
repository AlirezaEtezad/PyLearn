import turtle

def draw_dragon():
    window = turtle.Screen()
    window.bgpic("dragon.png")  # Replace with the actual dragon image file path

def draw_happy_1403():
    happy_1403_pen = turtle.Turtle()
    happy_1403_pen.speed(0)
    happy_1403_pen.color("black")
    happy_1403_pen.penup()
    happy_1403_pen.hideturtle()
    happy_1403_pen.goto(-100, 0)

    text = "Happy 1403"

    for char in text:
        happy_1403_pen.write(char, align="left", font=("Arial", 30, "bold"))
        happy_1403_pen.forward(20)

def main():
    draw_dragon()
    draw_happy_1403()

    turtle.done()

if __name__ == "__main__":
    main()
