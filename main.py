from turtle import *
color("orange")
forward(50)
left(90)
forward(50)
right(90)
forward(50)

forward(100)

color("red")
left(90)
forward(100)

reset()
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

done()

