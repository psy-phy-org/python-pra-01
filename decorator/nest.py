# coding=utf-8
# pylint: disable=invalid-name
"""関数のネスト"""

def outer(x):
    def inner():
        print(x)
    inner()

outer(2)
