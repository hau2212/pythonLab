"""
nguyen thanh hau
24-0-00627
ve ma tran
"""
import turtle

def veHinhRua():
    canh = 10
    t = turtle.Turtle()
    t.speed(0)
    for point in range(20):
        t.forward(canh)
        t.left(90)
        canh += 10

veHinhRua()
turtle.done()
