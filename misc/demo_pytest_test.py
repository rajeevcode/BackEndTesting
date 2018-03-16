"""
This file is to demo the use of 'py.test' test runner

Two functions are defined. One that adds two numbers passed in as parameters, and another that multiplies
two numbers.

Then four test functions are defined, that test the two functions.
"""


def my_adder(a, b):
    """
    Function that will add two parameters and return the result
    :param a:
    :param b:
    :return:
    """
    c = a + b
    return c


def my_multiplier(x, y):
    """
    Function that will multiply two parameters and return the result.
    :param x:
    :param y:
    :return:
    """
    z = x * y
    return z


def test_tc1_adder():
    """
    Function to test our adding function.
    :return:
    """
    assert my_adder(1,1) == 2, 'TC1 sum is not correct'


def test_tc2_adder():
    """
    Function to test our adding function.
    :return:
    """
    assert my_adder(1,1) == 11, '11 is not good'


def test_tc3_multiplier():
    """
    Function to test our multiplier function.
    :return:
    """
    assert my_multiplier(10,10) == 100, 'TC3 multiplier is not correct'


def test_tc4_multiplier():
    """
    Function to test our multiplier function.
    :return:
    """
    assert my_multiplier(2,3) == 6, 'TC4 multiplier is not correct'
