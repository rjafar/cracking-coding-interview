import pytest
from myStack import MyStack

def test_push():
    s = MyStack()
    assert 1 == s.push(1)
    assert 2 == s.push(2)
    assert 2 == s.size()

def test_pop():
    s = MyStack()
    s.push(1)
    s.push(2)
    assert 2 == s.pop()
    assert 1 == s.pop()

def test_size():
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert 3 == s.size()
    s.pop()
    assert 2 == s.size()
    s.push(4)
    assert 3 == s.size()

def test_empty():
    s = MyStack()
    assert 1 == s.isEmpty()
    s.push(1)
    assert 0 == s.isEmpty()
    s.pop()
    assert 1 == s.isEmpty()

def test_peek():
    s = MyStack()
    s.push(1)
    s.push(2)
    assert 2 == s.peek()
    s.push(3)
    assert 3 == s.peek()
    s.pop()
    assert 2 == s.peek()
