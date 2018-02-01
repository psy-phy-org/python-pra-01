# coding=utf-8
# pylint: disable=invalid-name
"""デコレータ"""


def decorator(fn):
    def wrapper(*args, **kwargs):
        print('---start: ' + fn.__name__)
        res = fn(*args, **kwargs)
        print('---end: ' + fn.__name__)
        return res
    return wrapper


@decorator
def foo(x, y, z):
    print(x * y - z)

foo(2, 3, 1)
