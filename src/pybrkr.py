
import typing as t

class PyBrkr():
    """
    The PyBrkr circuit-breaker is a decorator. It wraps whatever
    function call you want to protect.
    """
    def __init__(self, fn: t.Callable):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

