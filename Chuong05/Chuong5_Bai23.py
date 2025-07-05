"""
nguyen thanh hau
24-0-00627
chuong 5 bai 23
"""
import turtle

import turtle

def draw_circle(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(radius)

def drawBase():
    draw_circle(0, -160, 80)

def drawMidSection():
    draw_circle(0, 0, 60)

def drawHead():
    draw_circle(0, 120, 40)

    # Mắt
    turtle.penup()
    turtle.goto(-15, 145)
    turtle.dot(5)

    turtle.goto(15, 145)
    turtle.dot(5)

    # Miệng (đường thẳng)
    turtle.penup()
    turtle.goto(-15, 125)
    turtle.pendown()
    turtle.goto(15, 125)

def drawArms():
    # Tay trái
    turtle.penup()
    turtle.goto(-60, 60)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(40)
    # Nhánh tay
    turtle.backward(20)
    turtle.left(30)
    turtle.forward(10)
    turtle.backward(10)
    turtle.right(60)
    turtle.forward(10)

    # Tay phải
    turtle.penup()
    turtle.goto(60, 60)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(40)
    # Nhánh tay
    turtle.backward(20)
    turtle.right(30)
    turtle.forward(10)
    turtle.backward(10)
    turtle.left(60)
    turtle.forward(10)

def drawHat():
    # Vành mũ
    turtle.penup()
    turtle.goto(-50, 160)
    turtle.setheading(0)
    turtle.color("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()

    # Mũ đứng
    turtle.penup()
    turtle.goto(-25, 170)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
    turtle.end_fill()

def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.bgcolor("lightblue")
    turtle.color("black")

    drawBase()
    drawMidSection()
    drawHead()
    drawArms()
    drawHat()

    turtle.done()

main()

