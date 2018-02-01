# coding=utf-8
# pylint: disable=invalid-name
""""任意の数の必須パラメータを受けとるデコレータ"""
import functools

def decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        """デコレータのDocstring"""
        print('---start: ' + fn.__name__)
        res = fn(*args, **kwargs)
        print('---end: ' + fn.__name__)
        return res
    return wrapper

@decorator
def foo(**kwargs):
    """デコレートする関数のDocstring"""
    for a in kwargs:
        print(a, kwargs[a])

if __name__ == '__main__':
    foo(name="Yamada", age=18, role=1)

    print(foo.__name__)
    print(foo.__doc__)
