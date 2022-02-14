"""
Tests the pybrkr.py module.
"""

from src.pybrkr import PyBrkr

SUCCESS_RESP = "success"
OPEN_RESP = "open"


def function(succeed: bool = True):
    """
    A function to test out our circuit-breaker on.

    For now, we assume that any exception raised is what counts as an error. This
    will change.
    """
    if succeed:
        return SUCCESS_RESP
    else:
        raise Exception("Failed function call.")


def test_success():
    """
    Merely tests that the decorator can wrap a function.
    """
    assert PyBrkr(function)(succeed=True) == SUCCESS_RESP


def test_failure():
    """
    Merely tests that the decorator can handle its wrapped function's failure.
    """
    assert PyBrkr(function, open_resp=OPEN_RESP)(succeed=False) == OPEN_RESP
