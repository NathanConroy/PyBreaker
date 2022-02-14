
import typing as t

class PyBrkr():
    """
    The PyBrkr circuit-breaker is a decorator. It wraps whatever
    function call you want to protect.
    """
    def __init__(
        self,
        fn: t.Callable,
        open_resp: t.Optional[t.Any] = None,
    ):
        self._fn = fn
        self._open_resp = open_resp

    def __call__(self, *args, **kwargs):
        try:
            # Success.
            return self._fn(*args, **kwargs)
        except Exception:
            # Failure.
            #
            # Eventually clients will be able to specify
            # what counts as a failure. But for now, all
            # exceptions will be considered failures.
            return self._open_resp

