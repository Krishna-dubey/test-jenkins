import unittest
from circle_area import circleArea
from math import pi

class TestCircleArea(unittest.TestCase):
	def test_area(self):
		#Testing area when radius >= 0
		self.assertAlmostEqual(circleArea(1),pi)
		self.assertAlmostEqual(circleArea(0),0)
		self.assertAlmostEqual(circleArea(3.3),pi*3.3*3.3)

	def test_radius_values(self):
		#Raise value error if neccessary
		self.assertRaises(ValueError,circleArea, -2)

	def test_radius_values_types(self):
		#Raise type error if neccessary
		self.assertRaises(TypeError,circleArea, "r")
		self.assertRaises(TypeError,circleArea, True)
		self.assertRaises(TypeError,circleArea, 3+5j)

