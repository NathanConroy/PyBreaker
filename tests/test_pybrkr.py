"""
Tests the pybrkr.py module.
"""

from src.pybrkr import PyBrkr

SUCCESS_RESP = "success"


def function(succeed=True):
    """
    A function to test out our circuit-breaker on.

    For now, we assume that any exception raised is what counts as an error. This
    will change.
    """
    if succeed:
        return SUCCESS_RESP
    else:
        raise Exception("Failed function call.")


def test_decorator_init():
    """
    Merely tests that the decorator can wrap a function.
    """
    assert PyBrkr(function)() == SUCCESS_RESP
