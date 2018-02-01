# coding=utf-8
# pylint: disable=invalid-name
"""クロージャー"""

def outer(x):
    def inner():
        print(x)
    return inner

foo1 = outer(1)
foo2 = outer(2)

foo1()
foo2()
