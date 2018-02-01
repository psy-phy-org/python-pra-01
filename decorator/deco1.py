# coding=utf-8
# pylint: disable=invalid-name
"""デコレータ"""


def decorator(fn):
    def wrapper():
        print('---start: ' + fn.__name__)
        fn()
        print('---end: ' + fn.__name__)
    return wrapper


def foo():
    print('Hello Decorator')

decorated = decorator(foo)

decorated()
