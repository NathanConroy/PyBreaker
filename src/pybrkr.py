import typing as t


class TripCond():
    """
    This is the base class for circuit breaker trip conditions.

    In the future, this class will be abstract and PyBrkr will
    require a child class.
    """

    def __init__(self):
        self.max_failure = 0
        self.fail_cnt = 0

    def incr_fail(self):
        self.fail_cnt += 1

    def should_trip(self):
        return self.fail_cnt >= self.max_failure


class PyBrkr():
    """
    The PyBrkr circuit-breaker is a decorator. It wraps whatever
    function call you want to protect.
    """
    def __init__(
        self,
        trip_cond: t.Optional[TripCond] = None,
        open_resp: t.Optional[t.Any] = None,
    ):
        _check_args(trip_cond)
        self._trip_cond = trip_cond if trip_cond else TripCond()
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
                self._trip_cond.incr_fail()
                if self._trip_cond.should_trip():
                    return self._open_resp
                else:
                    return self(fn)
        return wrapper

def _check_args(trip_cond: TripCond):
    if trip_cond and not isinstance(trip_cond, TripCond):
        raise TypeError(f"The given trip_cond is not a TripCond.")
