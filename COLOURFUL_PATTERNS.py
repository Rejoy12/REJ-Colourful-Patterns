import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)  


colors = ["red", "orange", "yellow", "green", "blue", "purple"]


for i in range(360):
    pen.pencolor(colors[i % 6])  
    pen.width(i / 100 + 1)  
    pen.forward(i)  
    pen.left(59)  


pen.hideturtle()
turtle.done()

