'''Importing required module'''
import unittest
from math import pi
from circle_area import circle_area

class TestCircleArea(unittest.TestCase):
    '''Class to unit test circle_area function'''
    def test_area(self):
        '''Testing area when radius >= 0'''
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(3.3), pi*3.3*3.3)

    def test_radius_values(self):
        '''Raise value error if neccessary'''
        self.assertRaises(ValueError, circle_area, -2)

    def test_radius_values_types(self):
        '''Raise type error if neccessary'''
        self.assertRaises(TypeError, circle_area, "r")
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, 3+5j)
		