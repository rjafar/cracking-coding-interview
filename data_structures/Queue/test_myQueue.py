import pytest
from myQueue import MyQueue

def test_enqueue():
    q = MyQueue()
    assert 2 == q.enqueue(2)
    assert 1 == q.size()
    assert 5 == q.enqueue(5)
    assert 2 == q.size()
    
def test_dequeue():
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert 2 == q.size()
    assert 1 == q.dequeue()
    assert 1 == q.size()
    assert 2 == q.dequeue()
    assert 0 == q.size()
    assert 1 == q.isEmpty()

def test_size():
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert 3 == q.size()
    q.enqueue(4)
    assert 4 == q.size()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    assert 1 == q.size()

def test_empty():
    q = MyQueue()
    assert 1 == q.isEmpty()
    q.enqueue(1)
    assert 0 == q.isEmpty()