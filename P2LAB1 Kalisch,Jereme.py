# Jereme Kalisch
# 09/30/2024
# P2LAB1
# Using the radius, program will calculate the diameter, circumference, and area of a circle.
# with f-string

import math
print()
print()
print('Lets find the Diameter, Circumference, and Area of a Circle!!')
print()
print()

# Find the radius of the circle, needs to be a float.
radius = float(input('What is the radius of the circle? '))

print()
# Find the diameter of the circle, formatted with one after decimal
diameter = (2*radius)
print(f'The Diameter of the circle is: {diameter:.1f}')

print()
# Find the circumference of the circle, should have two after decimal
circumference =(2*math.pi*radius)
print(f'The circumference of the circle is: {circumference:.2f}')
print()
# Get the area of the circle, should have 3 after the decimal.
area = (math.pi*pow(radius,2))
print(f'The area of the circle: {area:.3f}')
print()
