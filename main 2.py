import turtle
from turtle import *
letter_size = 30
gap = 10

# H
pendown()
left(90)
forward(letter_size * 2)
backward(letter_size)
right(90)
forward(letter_size)
left(90)
forward(letter_size)
backward(letter_size * 2)
right(90)
penup()
forward(gap)

# e
pendown()
left(90)
forward(letter_size)
right(90)
forward(letter_size)
right(90)
forward(letter_size / 2)
right(90)
forward(letter_size)
left(90)
forward(letter_size / 2)
left(90)
forward(letter_size)
penup()
forward(gap)

# l
pendown()
left(90)
forward(letter_size * 2)
right(90)
penup()
forward(gap)

# l
pendown()
right(90)
forward(letter_size * 2)
left(90)
penup()
forward(gap)

# o
pendown()
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)

reset()

screen= turtle.Screen()
t=turtle.Turtle()
t.color("white")
t.hideturtle()

t.penup()
t.goto(-100,0)
t.write ("I'm Michael",font=("Arial",48,"normal"))
done()
