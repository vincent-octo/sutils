from decorator import decorator
import os


def fork(n):
    """Decorator to fork a function many times.

    :param int n: number of forks to make.
    :returns: None

    Example
    -------
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
