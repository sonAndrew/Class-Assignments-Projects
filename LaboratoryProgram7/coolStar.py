from turtle import Turtle, tracer, update
import turtle
def cCurve(t, x1, y1, z1, level):
    def drawLine3(z1):
        z2 = z1 / 3 # 40
        z3 = (z1 / 2) + z2 # 60
        t.forward(z2)
        t.left(z3)
        t.forward(z2)
        t.right(z1)
        t.forward(z2)
        t.left(z3)
        t.forward(z2)
        t.left(z3)
        t.forward(z2)
        t.left(z3)
        t.forward(z2)
        t.right(z1)
    if level == 0:
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)

def main():
    level = int(input("Enter the level (0 or greater): "))
    t = Turtle()
    if level > 8:
        tracer(False)
    t.pencolor("blue")
    t.hideturtle()
    cCurve(t, 0, -120, 120, level)
    if level > 8:
        update()
    
    turtle.done()

if __name__ == "__main__":
    main()
