"""
Unit tests for the calculator library
"""

import calculate


class TestCalculator:

    def test_addition(self):
        assert 4 == calculate.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculate.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculate.multiply(10, 10)

    def test_division(self):
        assert 1 == calculate.division(10, 10)
