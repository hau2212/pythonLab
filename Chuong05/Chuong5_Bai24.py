"""
nguyen thanh hau
24-0-00627
chuong 5 bai 24.py

"""
import turtle

def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def drawPattern(width, height):
    layers = min(width, height) // 20  # số lớp lồng nhau, mỗi lớp cách 10px

    x = -width // 2
    y = height // 2

    for i in range(layers):
        w = width - i * 20
        h = height - i * 20
        draw_rectangle(x + i * 10, y - i * 10, w, h)

def main():
    turtle.speed(0)
    turtle.pensize(2)
    turtle.bgcolor("lightblue")

    # Nhập chiều rộng và chiều cao từ người dùng
    width = int(input("Nhập chiều rộng mẫu: "))
    height = int(input("Nhập chiều cao mẫu: "))

    drawPattern(width, height)

    turtle.hideturtle()
    turtle.done()

main()
