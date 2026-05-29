import addition
import pytest


def test_add():
    assert addition.add(4, 5) == 9


def test_sub_function():
    assert addition.sub(3, 2) == 1
