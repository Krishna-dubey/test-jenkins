'''Importing constant pi from math module
   to be used in area of circle formula'''
from math import pi

def circle_area(radius):
    '''Defining function which returns area of circle
   by taking radius as input'''
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be non-negative real number")
    if radius < 0:
        raise ValueError("The radius cannot be negative")
    return pi*(radius*radius)
