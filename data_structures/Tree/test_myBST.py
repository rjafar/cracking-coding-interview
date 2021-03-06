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

def test_isBalanced():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    result = Node.isBalanced(Node, root)
    assert result == True
    root.left.left = Node(4)
    root.left.left.left = Node(5)
    result = Node.isBalanced(Node, root)
    assert result == False
    root.left.right = Node(6)
    result = Node.isBalanced(Node, root)
    assert result == False
    root.right.right = Node(7)
    result = Node.isBalanced(Node, root)
    assert result == True

def test_validBST():
    root = Node(10)
    root.left = Node(5)
    root.left.right = Node(15)
    root.right = Node(20)
    result = Node.isValidBST(Node, root)
    assert result == False
    root.left.right = Node(7)
    result = Node.isValidBST(Node, root)
    assert result == True

def test_successor():
    root = Node(5)
    root.left = Node(3)
    root.left.parent = root
    root.right = Node(10)
    root.right.parent = root
    root.left.right = Node(4)
    root.left.right.parent = root.left
    root.right.left = Node(7)
    root.right.left.parent = root.right
    root.right.right = Node(15)
    root.right.right.parent = root.right
    result = Node.findSuccessor(Node, root.left.right) # 4
    assert result.data == 5
    result = Node.findSuccessor(Node, root.left) # 3
    assert result.data == 4
    result = Node.findSuccessor(Node, root) # 5
    assert result.data == 7
    result = Node.findSuccessor(Node, root.right.right) # 15
    assert result.data == 15

def test_ancestor():
    root = Node(10)
    root.left = Node(20)
    root.left.parent = root
    root.right = Node(7)
    root.right.parent = root
    root.left.left = Node(5)
    root.left.left.parent = root.left
    root.left.right = Node(15)
    root.left.right.parent = root.left
    result = Node.findCommonAncestor(Node, root.left.left, root.right)
    assert result.data == 10
    result = Node.findCommonAncestor(Node, root, root.left.left)
    assert result.data == 10
    result = Node.findCommonAncestor(Node, root.left.left, root.left.right)
    assert result.data == 20
    result = Node.findCommonAncestor(Node, root.right, root.right)
    assert result.data == 7