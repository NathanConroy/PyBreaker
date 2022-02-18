"""
Tests the pybrkr.py module.
"""
import pytest

from src.pybrkr import PyBrkr

SUCCESS_RESP = "success"
OPEN_RESP = "open"


def test_fn(succeed: bool = True):
    """
    A function to test out our circuit-breaker on.

    For now, we assume that any exception raised is what counts as an error. This
    will change.
    """
    if succeed:
        return SUCCESS_RESP
    else:
        raise Exception("Failed function call.")


@PyBrkr(open_resp=OPEN_RESP)
def pybrkr_fn(succeed: bool):
    return test_fn(succeed)


def test_success():
    """
    Merely tests that the decorator can wrap a function.
    """
    assert pybrkr_fn(succeed=True) == SUCCESS_RESP


def test_failure():
    """
    Merely tests that the decorator can handle its wrapped function's failure.
    """
    assert pybrkr_fn(succeed=False) == OPEN_RESP


def test_trip_cond_bad_type():
    """
    Test passing a non-trip condition as a PyBrkr trip_cond.
    """
    with pytest.raises(TypeError):
        @PyBrkr(trip_cond=object())
        def func():
            return test_fn()
