"""
nguyen thanh hau
24-0-00627
chuong 5 bai 25
"""

import turtle

def drawSquare(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("black", color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def drawChessBoard():
    square_size = 40
    start_x = -square_size * 4
    start_y = square_size * 4

    colors = ["lightblue", "black"]

    for row in range(8):
        for col in range(8):
            x = start_x + col * square_size
            y = start_y - row * square_size
            color = colors[(row + col) % 2]
            drawSquare(x, y, square_size, color)

def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")
    drawChessBoard()
    turtle.done()

main()
