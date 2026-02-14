#TurtleGraphics.py
#Name:Carter Guthrie
#Date:2/13/2025
#Assignment: Lab 4

import turtle

t = turtle.Turtle()
t.speed(3) 
screen = turtle.Screen()
screen.bgcolor("skyblue")

'
t.penup()
t.goto(-400, -100) 
t.pendown()

t.fillcolor("blue") 
t.begin_fill()      
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(300)
    t.right(90)
t.end_fill()

t.penup()
t.goto(0, 50)
t.color("yellow")
t.dot(100) 


t.penup()
t.goto(-100, 150)
t.shape("classic") 
t.color("black")
t.stamp()         

turtle.done()