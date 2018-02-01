# coding=utf-8
# pylint: disable=invalid-name
""""任意の数の必須パラメータを受けとるデコレータ"""

def decorator(fn):
    def wrapper(*args, **kwargs):
        print('---start: ' + fn.__name__)
        res = fn(*args, **kwargs)
        print('---end: ' + fn.__name__)
        return res
    return wrapper

@decorator
def foo(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])

foo(name="Yamada", age=18, role=1)
