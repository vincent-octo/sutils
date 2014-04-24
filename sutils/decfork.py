from decorator import decorator
import os


__all__ = ['fork']


def fork(n):
    """Decorator to fork a function many times.

    :param int n: number of forks to make.
    :returns: None

    *Example*

        >>> from time import sleep
        >>> @fork(n=3)
        ... def my_func_to_fork():
        ...     print('Starting...')
        ...     sleep(1)
        ...     print('done')
        >>> my_func_to_fork()

    will output ::

        'Starting...'
        'Starting...'
        'Starting...'
        'done'
        'done'
        'done'

    """
    # Check that we passed a correct value for n
    if not isinstance(n, int):
        raise TypeError('Argument of fork should be an integer, not %s.' % type(n))
    else:
        if not n > 0:
            raise ValueError('Argument n of fork should be greater than 0, not %d.' % n)

    @decorator
    def wrapper(f, *args, **kwargs):
        # Actual function that will make the forks.
        children = []

        # Make n forks, run the desired function on each one.
        for _ in xrange(n):
            pid = os.fork()
            if pid:
                children.append(pid)
            else:
                f(*args, **kwargs)
                os._exit(0)  # exit child fork

        # Make sure each child has finished its job
        for child in children:
            os.waitpid(child, 0)

    return wrapper
