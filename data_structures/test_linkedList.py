import pytest
from linkedList import LinkedList

def test_insert():
    LL = LinkedList()
    LL.insert(1)
    assert 1 == LL.find(1)

    LL.insert(2)
    assert 2 == LL.find(2) 
    assert 1 == LL.find(1)

def test_find():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    assert None == LL.find(3)

def test_remove():
    LL = LinkedList()
    LL.insert(1)
    LL.remove(1)
    assert None == LL.find(1)

def test_size():
    LL = LinkedList()
    LL.insert(1)
    assert 1 == LL.size()

    LL.remove(1)
    assert 0 == LL.size()