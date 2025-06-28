import turtle
t = turtle.Turtle()
diThanh = 10
def veTurtle():
    while True:
        global diThanh

        for i in range(4):
            t.forward(diThanh)
            t.left(90)
        diThanh += 10

veTurtle()
turtle.done()