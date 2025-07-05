"""
nguyen thanh hau
24-0-00627
chuong 5 bai 26
"""

import turtle
import random

# === Vẽ hình chữ nhật (tòa nhà hoặc cửa sổ) ===
def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

# === Vẽ bầu trời và các ngôi sao ===
def draw_sky_and_stars():
    turtle.bgcolor("black")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color("white")

    # Vẽ 30 ngôi sao ngẫu nhiên phía trên màn hình
    for _ in range(30):
        x = random.randint(-300, 300)
        y = random.randint(50, 250)  # chỉ vẽ trên bầu trời, không dính vào tòa nhà
        turtle.penup()
        turtle.goto(x, y)
        turtle.dot(random.randint(2, 5), "white")

# === Vẽ các tòa nhà ===
def draw_buildings():
    building_colors = ["gray", "dimgray", "slategray"]

    buildings = [
        (-300, -200, 100, 150),
        (-180, -200, 80, 220),
        (-80, -200, 100, 180),
        (40, -200, 80, 250),
        (140, -200, 100, 170),
        (260, -200, 80, 200)
    ]

    for b in buildings:
        x, y, w, h = b
        color = random.choice(building_colors)
        draw_rectangle(x, y, w, h, color)
        draw_windows(x, y, w, h)

# === Vẽ các cửa sổ cho từng tòa nhà ===
def draw_windows(x, y, w, h):
    turtle.color("yellow")
    num_windows = random.randint(4, 8)
    for _ in range(num_windows):
        win_x = random.randint(x + 5, x + w - 15)
        win_y = random.randint(y + 10, y + h - 15)
        draw_rectangle(win_x, win_y, 10, 10, "yellow")

# === Chạy chương trình chính ===
def main():
    turtle.setup(700, 500)
    draw_sky_and_stars()
    draw_buildings()
    turtle.done()

main()
