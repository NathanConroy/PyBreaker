"""
Tests the pybrkr.py module.
"""

from src.pybrkr import PyBrkr

TEST_RET_VAL = "hello world"


def function():
    """
    A function to test out our circuit-breaker decorator on.
    """
    return TEST_RET_VAL 


def test_decorator_init():
    """
    Merely tests that the decorator can wrap a function.
    """
    assert PyBrkr(function)() == TEST_RET_VAL

