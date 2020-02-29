import pytest
from linkedList import Node
from linkedList import LinkedList
from intersection import intersection

def test_diff_len_intersection():
    LL = LinkedList()
    LL2 = LinkedList()

    node = Node(4)
    node2 = Node(5)

    LL.head = Node(1)
    LL.head.next = node
    LL.head.next.next = node2

    LL2.head = Node(10)
    LL2.head.next = Node(11)
    LL2.head.next.next = node
    LL2.head.next.next.next = node2

    assert node == intersection(LL, LL2)

def test_same_len_intersection():
    LL = LinkedList()
    LL2 = LinkedList()

    node = Node(4)
    node2 = Node(5)

    LL.head = Node(1)
    LL.head.next = Node(7)
    LL.head.next.next = node
    LL.head.next.next.next = node2

    LL2.head = Node(10)
    LL2.head.next = Node(11)
    LL2.head.next.next = node
    LL2.head.next.next.next = node2

    assert node == intersection(LL, LL2)

def no_intersection():
    LL = LinkedList()
    LL2 = LinkedList()

    LL.head = Node(1)
    LL.head.next = Node(7)
    LL.head.next.next = Node(5)
    LL.head.next.next.next = Node(4)

    LL2.head = Node(1)
    LL2.head.next = Node(7)
    LL2.head.next.next = Node(5)
    LL2.head.next.next.next = Node(4)

    assert None == intersection(LL, LL2)