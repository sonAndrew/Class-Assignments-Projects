from turtle import Turtle, tracer, update
import turtle

def cCurve(t, x1, y1, z1, level):
    """Draws a c-curve of the given level"""
    t.up()
    t.goto(x1, y1) # -120, 0
    t.down()
    def drawLine(z1):
        t.forward(z1) # 120
        t.right(z1) # 120
        t.forward(z1) # 120
        t.right(z1) # 120
        t.forward(z1) # 120

    def drawLine2(z1):
        z2 = z1 / 2 # 60
        
        t.forward(z2) # 60
        t.left(z2) # 60
        t.forward(z2) # 60
        t.right(z1) # 120

    def drawLine3(z1):
        z2 = z1 / 3 # 40
        z3 = (z1 / 4) + z2 # 90
        t.forward(z2) # 60
        t.left(z2) # 60
        t.forward(z2) # 60
        t.right(z3) # 120

    if level == 0:
        drawLine(z1)

    elif level == 1:
        drawLine2(z1)
        drawLine2(z1)
        drawLine2(z1)
        drawLine2(z1)
        drawLine2(z1)
        drawLine2(z1)
        drawLine2(z1)
        drawLine2(z1)

    elif level == 2:
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
        drawLine3(z1)
    
    else:
        print("Other")


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
