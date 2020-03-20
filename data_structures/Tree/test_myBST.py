import pytest
from myBST import Node

#        3
#      /   \
#     1     5
#      \   / \
#       2  4  10
root = Node(3)
root.insert(root,Node(1))
root.insert(root,Node(5))
root.insert(root,Node(10))
root.insert(root,Node(2))
root.insert(root,Node(4))

def test_insert():
    assert root.data == 3
    assert root.left.data == 1
    assert root.left.right.data == 2
    assert root.right.data == 5
    assert root.right.left.data == 4
    assert root.right.right.data == 10

def test_search():
    result = root.search(root, 10)
    assert 10 == result.data
    result = root.search(root, 9)
    assert None == result

def test_remove_leaf():
    root.remove(root,2)
    root.inorder(root)
    assert root.data == 3
    assert root.left.data == 1
    assert root.left.right == None # removed
    assert root.right.data == 5
    assert root.right.left.data == 4
    assert root.right.right.data == 10

def test_remove_one_child():
    root.insert(root,Node(2))
    root.remove(root,1)
    root.inorder(root)
    assert root.data == 3
    assert root.left.data == 2
    assert root.left.right == None
    assert root.right.data == 5
    assert root.right.left.data == 4
    assert root.right.right.data == 10

def test_remove_two_child():
    root.remove(root,3)
    root.inorder(root)
    assert root.data == 4
    assert root.left.data == 2
    assert root.left.right == None
    assert root.right.data == 5
    assert root.right.left == None
    assert root.right.right.data == 10

def test_minBST():
    array = [1,2,3,4,5,6,7]
    result = Node.createMinBST(Node, array)
    assert root.data == 4
    assert root.left.data == 2
    assert root.left.left.data == 1
    assert root.left.right.data == 3
    assert root.right.data == 6
    assert root.right.left.data == 5
    assert root.right.right.data == 7

def test_listOfDepths():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)

    result = Node.listOfDepths(Node, root)
    assert result[0][0].data == 1
    assert result[1][0].data == 2
    assert result[1][1].data == 3
    assert result[2][0].data == 4
    assert result[2][1].data == 5
    assert result[2][2].data == 6