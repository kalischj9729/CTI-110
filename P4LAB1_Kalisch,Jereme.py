# Jereme Kalisch
# 10/28/2024
# P4LAB1 
# Using turtle to create an object

import turtle
win =turtle.Screen()
t = turtle.Turtle()

# add some display options
t.pensize(4)   #Increase pensize (takes interger)
t.pencolor("orange")   # Set the pencolor (takes string)

# Commands from here to last line can be replaced
# Pentagon, sides are 360 / 5 = 72 degrees

t.left(180)   #this time we'll draw it in a differenet

# Draw the pentagon
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
# End of pentagon

# Start for square
t.pensize(6)
t.pencolor("red")
t.shape("turtle")
# Line for diffent start
t.right(100)
t.forward(150)
# Begin the square.
t.right(90)
t.forward(100)
# While loop to draw 4 sides of a square
line = 0
while line < 3:
    t.left(90)
    t.forward(100)
    line += 1
'''
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''
# End of the square, start of the triangle.
t.pencolor("yellow")
#
for line1 in range(3):
    t.right(120)
    t.forward(100)
'''
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)
'''
'''
# While loop to draw 4 sides of a square
line = 0
while line < 4:
    t.right(90)
    t.forward(150)
    line += 1

# For loop to draw triangle
for line1 in range(3):
    t.left(120)
    t.forward(150)

'''
