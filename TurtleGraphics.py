#TurtleGraphics.py
#Name:Carter Guthrie
#Date:2/13/2025
#Assignment: Lab 4

import turtle

# 1. Required: Simple square function
def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

# 2. Required: Polygon function
def drawPolygon(t, sides, size):
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.left(angle)

# 3. Fixed: Uses a corner_num parameter (1, 2, 3, or 4)
def fillCorner(t, size, corner_num):
    drawSquare(t, size) # Draw the big square
    
    t.begin_fill()
    # Logic to pick which quadrant to fill
    if corner_num == 1:
        drawSquare(t, size / 2)
    elif corner_num == 2:
        t.forward(size / 2)
        drawSquare(t, size / 2)
    elif corner_num == 3:
        t.penup()
        t.goto(t.xcor() + size/2, t.ycor() + size/2)
        t.pendown()
        drawSquare(t, size / 2)
    elif corner_num == 4:
        t.left(90)
        t.forward(size / 2)
        t.right(90)
        drawSquare(t, size / 2)
    t.end_fill()

# 4. Required: Nested squares
def squaresInSquares(t, num, size):
    for i in range(num):
        drawSquare(t, size)
        size -= 20 # Make the next one smaller

def main():
    bob = turtle.Turtle()
    bob.speed(0) # Makes it draw fast
    
    # Test the functions
    drawSquare(bob, 50)
    
    bob.penup()
    bob.goto(-100, -100)
    bob.pendown()
    bob.fillcolor("red")
    fillCorner(bob, 100, 3) # Fills corner #3
    
    bob.penup()
    bob.goto(100, 100)
    bob.pendown()
    squaresInSquares(bob, 5, 120)

if __name__ == "__main__":
    main()