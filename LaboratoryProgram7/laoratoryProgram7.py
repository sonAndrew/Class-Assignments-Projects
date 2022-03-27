"""
    Author    :  Andrew Jackson
    Class     :  Intorduction to Computing and Programming Concepts
    Section   :  CSCI 1523-92
    File      :  laboratoryProgram7.py
    Date Due  :  03/27/2022
    Professor :  Phil Lamb
    About     :  Create the first three levels of a Koch snowflake
"""
from turtle import Turtle, tracer, update      # Import Turtle, tracer, and update from the turtle module 
import turtle                                  # Import turtle 

# Create function called ( cCurve ) with parameters ( t, x1, y1, z1, level )
def cCurve(t, x1, y1, z1, level):
    """Draws a c-curve of the given level"""
    t.up()                                      # Moves the turtle up off of the page
    t.goto(x1, y1) # -120, 0                    # Moves the turtle to the cordinates
    t.down()                                    # Moves the turtle down to the page

    # Create a function that creates an ( Upside Down Triangle ) - The first level of a Koch snowflake
    def upsideDownTriangle(z1):
        t.forward(z1) # 120                     # Moves the turtle forward
        t.right(z1) # 120                       # Turn the turtle right
        t.forward(z1) # 120                     # Moves the turtle forward
        t.right(z1) # 120                       # Turn the turtle right
        t.forward(z1) # 120                     # Moves the turtle forward

    # Create a function that creates a ( Hexagram ) - The second level of a Koch snowflake
    def hexagram(z1):
        # Variables
        z2 = z1 / 2 # 60                        # Creates a variable called ( z2 ) witch devides the ( parameter ) of the function in half
        
        t.forward(z2) # 60                      # Moves the turtle forward
        t.left(z2) # 60                         # Turn the turtle left
        t.forward(z2) # 60                      # Moves the turtle forward
        t.right(z1) # 120                       # Turn the turtle right

    # Create a function that creates the second level  - The third level of a Koch snowflake
    def levelThree(z1):
        # Variables
        z2 = (z1 / 2) # 60                      # Creates a variable called ( z2 ) witch devides the ( parameter ) of the function in half
        z3 = (z1 / 3) # 40                      # Creates a variable called ( z3 ) witch devides the ( parameter ) of the function by 3

        t.left(z2) # 60                         # Turn the turtle left
        t.forward(z3) # 40                      # Moves the turtle forward
        t.left(z2) # 60                         # Turn the turtle left
        t.forward(z3) # 40                      # Moves the turtle forward
        t.left(z2) # 60                         # Turn the turtle left
        t.forward(z3) # 40                      # Moves the turtle forward
        t.right(z1) # 120                       # Turn the turtle right
        t.forward(z3) # 40                      # Moves the turtle forward
        t.left(z2) # 60                         # Turn the turtle left
        t.forward(z3) # 40                      # Moves the turtle forward
        t.right(z1) # 120                       # Turn the turtle right
        t.forward(z3) # 40                      # Moves the turtle forward
        t.left(z2) # 60                         # Turn the turtle left
        t.forward(z3) # 40                      # Moves the turtle forward
        t.right(z1) # 120                       # Turn the turtle right
        t.forward(z3) # 40                      # Moves the turtle forward

    # If the level value is equal to ( Zero )
    if level == 0:
        upsideDownTriangle(z1)                  # Use the ( upsideDownTriangle ) function

    # Else, If the level value is equal to ( One )
    elif level == 1:
        hexagram(z1)                           # Use the ( hexagram ) function 8 times
        hexagram(z1)
        hexagram(z1)
        hexagram(z1)
        hexagram(z1)
        hexagram(z1)
        hexagram(z1)
        hexagram(z1)

    # Else, If the level value is equal to ( Two )
    elif level == 2:
        levelThree(z1)                           # Use the ( levelThree ) function 6 times
        levelThree(z1)
        levelThree(z1)
        levelThree(z1)
        levelThree(z1)
        levelThree(z1)
    # Else, print ( "Please enter a valid value" )
    else:
        print("Please enter a valid value")

# Main entry point function
def main():
    # Variables
    level = int(input("Enter the level ( 0, 1, 2): ")) # Get ( level ) value from the user, turn it into an integer and assign it to a variable called ( level )
    t = Turtle()                                       # Assigne ( Turtle() ) to a variable ( t )

    # If level is greater than 8
    if level > 8:
        tracer(False)                                  # tracer value is false

    t.pencolor("blue")                                 # turtle color is blue
    t.hideturtle()                                     # Hide the turtle
    cCurve(t, 0, -120, 120, level)                     # Use the ( cCurve ) function

    # If level is less than 8
    if level > 8:
        update()                                       # Update the view
    
    turtle.done()                                      # Keep the turtle window open after it's finished

# The entry point for program execution - Below
if __name__ == "__main__":
    main()
