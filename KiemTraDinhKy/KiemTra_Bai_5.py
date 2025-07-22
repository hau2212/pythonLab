"""
Nguyễn Thanh Hậu
kiểm tra định kỳ bài 5
Kiểm tra định kỳ - Câu 5: vẽ hình vuông turtle
"""

import turtle

# Vẽ một ô vuông tại (x, y) với kích thước size và màu fill color
def draw_square(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

#Vẽ bàn cờ 5x5 từ tọa độ bắt đầu
def draw_chessboard(top_left_x, top_left_y, square_size):
    colors = ["black", "lightblue"]
    for row in range(8):
        for col in range(8):
            x = top_left_x + col * square_size
            y = top_left_y - row * square_size
            color_index = (row + col) % 2  # xen kẽ màu
            draw_square(x, y, square_size, colors[color_index])

def main():
    turtle.speed(0)
    turtle.bgcolor("white")
    square_size = 60  # bạn có thể thay đổi kích thước này
    draw_chessboard(-150, 150, square_size)
    turtle.hideturtle()
    turtle.done()

main()
