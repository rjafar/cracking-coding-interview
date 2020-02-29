import pytest
from linkedList import Node
from linkedList import LinkedList
from loopDetection import loopDetection

def test_loop():
    LL = LinkedList()
    node = Node(3)

    LL.head = Node(1)
    LL.head.next = Node(2)
    LL.head.next.next = node
    LL.head.next.next.next = Node(4)
    LL.head.next.next.next.next = Node(5)
    LL.head.next.next.next.next = node

    assert node == loopDetection(LL)