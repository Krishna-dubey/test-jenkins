from math import pi

def circleArea(radius):
	if type(radius) not in [int,float]:
		raise TypeError("The radius must be non-negative real number")
	if radius<0:
		raise ValueError("The radius cannot be negative") 
	return pi*(radius*radius)
