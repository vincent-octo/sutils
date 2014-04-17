sutils -- Simple python utilities
=================================

Collection of Simple Python utilities.

This project is mainly used for benchmarking the [kTBS](https://github.com/ktbs/ktbs).


@bench -- Simple benchmark decorator
------------------------------------

This decorator let you time a function call.

For example, if you have some function:

```python
def my_function():
    # do some useful stuff
    return something

result = my_function()
```

you can time it by adding the `@bench` decorator:
```python
from sutils import bench

@bench
def my_function():
    # do some useful stuff
    return something

time, result = my_function()
```

As you can see, it changes what the function call returns.
It now returns a tuple of two elements. The first one is the time taken for the function call.
The second one is what the function returns normally (i.e. what we get if we don't use `@bench`).


@fork -- Fork made simple
-------------------------

Say you have function that you want to spawn on multiple processes.
All you have to do is:

```python
from sutils import fork

@fork(n=10)
def my_function():
    # do some stuff
```

where `n` is the number of forks you want.

This decorator use python [`os.fork`](https://docs.python.org/library/os.html#os.fork).
