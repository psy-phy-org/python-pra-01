# coding=utf-8
# pylint: disable=invalid-name
"""引数に関数を取る関数"""

def add(x ,y):
    return x + y

def sub(x, y):
    return x - y

def apply(func, x, y):
    return func(x, y)

foo = apply(add, 3, 1)
print(foo)
