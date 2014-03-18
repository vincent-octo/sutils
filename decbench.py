from decorator import decorator
from time import time


@decorator
def bench(f, *args, **kwargs):
    """Decorator to time a function.

    :param function f: The function to benchmark.
    :param list args: List of arguments for the function f.
    :param dict kwargs: Dictionnary of positional arguments for f.
    :returns: real time to execute f and result of f
    :rtype: tuple

    Example
    -------
    >>> from time import sleep
    >>> @bench
    ... def super_func(numbers):
    ...     sleep(1)
    ...     return numbers
    >>> bench_time, func_res = super_func([3, 4, 5])
    >>> 1. < bench_time < 1.1
    True
    >>> func_res
    [3, 4, 5]
    """
    tstart = time()
    res_func = f(*args, **kwargs)
    tstop = time()

    return tstop - tstart, res_func
