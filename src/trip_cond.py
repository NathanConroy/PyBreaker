

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
