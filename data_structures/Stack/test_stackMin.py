import pytest
from myStack import MyStack
from stackMin import StackMin

def test_min():
    s = StackMin()
    s.push(1)
    s.push(3)
    s.push(2)
    assert 1 == s.min()