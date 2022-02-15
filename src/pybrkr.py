
import typing as t

class PyBrkr():
    """
    The PyBrkr circuit-breaker is a decorator. It wraps whatever
    function call you want to protect.
    """
    def __init__(
        self,
        open_resp: t.Optional[t.Any] = None,
    ):
        self._open_resp = open_resp

    def __call__(self, fn: t.Callable):
        def wrapper(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception:
                # Failure.
                #
                # Eventually clients will be able to specify
                # what counts as a failure. But for now, only
                # exceptions will be considered failures.
                return self._open_resp
        return wrapper
