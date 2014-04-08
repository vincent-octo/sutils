from sutils import bench
import pytest


class TestBenchDecorator(object):

    def test_return_type(self):
        @bench
        def func_return_int():
            return 123

        res = func_return_int()
        assert isinstance(res, tuple)  # @bench should return a tuple of 2 elements
        assert len(res) == 2
        assert isinstance(res[0], float)  # the first one is the time in second
        assert isinstance(res[1], int)  # the second one is the result of the function
