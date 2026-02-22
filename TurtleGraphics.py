#TurtleGraphics.py
#Name:Carter Guthrie
#Date:2/13/2025
#Assignment: Lab 4

import turtle

# 1. First required function
def drawPolygon(t, sides):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(50)
        t.left(angle)

# 2. Second required function
def fillCorner(t, size):
    # Draw the big square
    for _ in range(4):
        t.forward(size)
        t.left(90)
    
    # Fill the small corner square
    t.begin_fill()
    for _ in range(4):
        t.forward(size / 2)
        t.left(90)
    t.end_fill()

# 3. Third required function
def squaresInSquares(t, num):
    size = 20
    for _ in range(num):
        for _ in range(4):
            t.forward(size)
            t.left(90)
        size += 20 # Make the next square bigger

def main():
    # Setup the turtle
    bob = turtle.Turtle()
    bob.speed(3)

    

    turtle.done()

if __name__ == "__main__":
    main()