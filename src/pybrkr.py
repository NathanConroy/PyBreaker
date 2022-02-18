import typing as t

import src.trip_cond as tc


class PyBrkr():
    """
    The PyBrkr circuit-breaker is a decorator. It wraps whatever
    function call you want to protect.
    """
    def __init__(
        self,
        trip_cond: t.Optional[tc.TripCond] = None,
        open_resp: t.Optional[t.Any] = None,
    ):
        _check_args(trip_cond)
        self._trip_cond = trip_cond if trip_cond else tc.TripCond()
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

def _check_args(trip_cond: tc.TripCond):
    if trip_cond and not isinstance(trip_cond, tc.TripCond):
        raise TypeError(f"The given trip_cond is not a TripCond.")
