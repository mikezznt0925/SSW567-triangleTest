# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    """Test cases for classifyTriangle(); IDs (T01, ...) map to the assignment test report."""

    # --- InvalidInput: out of range, non-positive, non-integer ---

    def test_T01_invalid_side_over_200(self):
        self.assertEqual(classifyTriangle(201, 1, 1), "InvalidInput")

    def test_T02_invalid_any_side_over_200(self):
        self.assertEqual(classifyTriangle(1, 200, 201), "InvalidInput")

    def test_T03_invalid_zero_side(self):
        self.assertEqual(classifyTriangle(0, 1, 1), "InvalidInput")

    def test_T04_invalid_negative_side(self):
        self.assertEqual(classifyTriangle(3, -1, 4), "InvalidInput")

    def test_T05_invalid_float_not_int(self):
        self.assertEqual(classifyTriangle(3.0, 4, 5), "InvalidInput")

    # --- NotATriangle: violates triangle inequality ---

    def test_T06_not_a_triangle_degenerate(self):
        self.assertEqual(classifyTriangle(1, 2, 3), "NotATriangle")

    def test_T07_not_a_triangle_one_side_too_long(self):
        self.assertEqual(classifyTriangle(1, 2, 4), "NotATriangle")

    def test_T08_not_a_triangle_ordering(self):
        self.assertEqual(classifyTriangle(10, 2, 3), "NotATriangle")

    # --- Equilateral ---

    def test_T09_equilateral_unit(self):
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral")

    def test_T10_equilateral_larger(self):
        self.assertEqual(classifyTriangle(5, 5, 5), "Equilateral")

    # --- Scalene (all sides different, valid triangle) ---

    def test_T11_scalene_234(self):
        self.assertEqual(classifyTriangle(2, 3, 4), "Scalene")

    def test_T12_scalene_346(self):
        self.assertEqual(classifyTriangle(3, 4, 6), "Scalene")

    # --- Isoceles (exactly two sides equal; not equilateral) ---

    def test_T13_isosceles_223(self):
        self.assertEqual(classifyTriangle(2, 2, 3), "Isoceles")

    def test_T14_isosceles_255(self):
        self.assertEqual(classifyTriangle(2, 5, 5), "Isoceles")

    def test_T15_isosceles_order_533(self):
        self.assertEqual(classifyTriangle(5, 3, 3), "Isoceles")

    # --- Right (Pythagorean triples; any side order) ---

    def test_T16_right_345(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right")

    def test_T17_right_534(self):
        self.assertEqual(classifyTriangle(5, 3, 4), "Right")

    def test_T18_right_51213(self):
        self.assertEqual(classifyTriangle(5, 12, 13), "Right")

    def test_T19_right_6810(self):
        self.assertEqual(classifyTriangle(6, 8, 10), "Right")

    def test_T20_right_hypotenuse_not_last(self):
        self.assertEqual(classifyTriangle(5, 13, 12), "Right")

    # --- Starter tests (kept as aliases for continuity) ---

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right", "3,4,5 is a Right triangle")

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), "Right", "5,3,4 is a Right triangle")

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1), "Equilateral", "1,1,1 should be equilateral")


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
