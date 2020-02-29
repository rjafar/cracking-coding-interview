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

# tests for removeDups
def test_noDups():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    assert LL == LL.removeDups()

def test_removeDups():
    LL = LinkedList()
    LL2 = LinkedList()
    LL.insert(2)
    LL.insert(2)
    LL.insert(1)
    LL.insert(1)
    LL2.insert(2)
    LL2.insert(1)
    assert print(LL2) == print(LL.removeDups())

# tests for kthToLast
def test_kthToLast():
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    LL.insert(4)
    assert 4 == LL.kthToLast(1)
    assert 1 == LL.kthToLast(4)
    assert None == LL.kthToLast(5)

# tests for delMidNode
def test_delMidNode():
    LL = LinkedList()
    LL.insert(1)
    Node2 = LL.insert(2)
    Node3 = LL.insert(3)
    LL.insert(4)

    LL2 = LinkedList()
    LL2.insert(1)
    LL2.insert(2)
    LL2.insert(4)
    assert print(LL2) == print(LL.delMidNode(Node3))
    LL2.remove(2)
    assert print(LL2) == print(LL.delMidNode(Node2))

# test partitionLL
def test_partitionLL():
    LL = LinkedList()
    LL.insert(10)
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    LL.insert(2)
    LL.insert(3)

    LL2 = LinkedList()
    LL2.insert(1)
    LL2.insert(2)
    LL2.insert(2)
    LL2.insert(10)
    LL2.insert(3)
    LL2.insert(3)
    assert print(LL2) == print(LL.partitionLL(3))
