from math import floor

# Implementation of a Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    # algorithm to create a BST with minimal height given a sorted array
    def createMinBST(self, array):
        if len(array) > 1:
            midIdx = floor(len(array)/2)
            print(array[midIdx])
            root = Node(array[midIdx])

            firstHalf = array[0 : midIdx]
            print(firstHalf)
            lastHalf = array[midIdx+1 : len(array)]
            print(lastHalf)

            root.left = self.createMinBST(self, firstHalf)
            root.right = self.createMinBST(self, lastHalf)

            return root
        else:
            return Node(array[0])


    # insert a node in the tree
    def insert(self, root, node):
        if not root: # if no root, the tree is empty so insert as root
            root = node
        else:
            if node.data < root.data: # if data is smaller than root, it belongs in left subtree
                if not root.left: # if no left child, insert
                    root.left = node
                else: # else keep recursing left subtree
                    self.insert(root.left, node)
            else: # same thing but for right subtree
                if not root.right:
                    root.right = node
                else:
                    self.insert(root.right, node)
    
    # Search and return a node from the tree
    def search(self, root, data):
        if not root or root.data == data: # empty tree or found at root
            return root
        elif data < root.data: # recurse left subtree
            return self.search(root.left, data)
        else: # recurse right subtree
            return self.search(root.right, data)

    # Traversals
    def inorder(self, root): # Left, Node, Right
        if root != None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root): # Node, Left, Right
        if root != None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root): # Left, Right, Node
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    # Remove a node from the BST and keep the property maintained. Return the new root.
    def remove(self, root, data):
        if root is None: # if empty, nothing to remove
            return None
        if data < root.data: # recurse left subtree
            root.left = self.remove(root.left, data)
        elif data > root.data: # recurse right subtree
            root.right = self.remove(root.right, data)
        else:
            if root.left == None: # if no left child, take data of right and relace root's data
                temp = root.right
                root = None
                return temp
            elif root.right == None: # same for if no right child
                temp = root.left
                root = None
                return temp

            temp = root.right # if both childrene exist, recurse right subtree to find left-most leaf
            while (temp.left):
                temp = temp.left
            root.data = temp.data
            root.right = self.remove(root.right, temp.data) # remove
        return root

    # Algorithm that creates a linked list of all nodes at each depth given a binary tree
    def listOfDepths(self, root):
        lists = []
        self.addLists(self, root, lists, 0)
        return lists

    def addLists(self, root, lists, level):
        if root is None: return

        if len(lists) == level:
            newList = []
            lists.append(newList)
        else:
            newList = lists[level]

        newList.append(root)
        level += 1

        self.addLists(self, root.left, lists, level)
        self.addLists(self, root.right, lists, level)

    # Algorithm to check whether a tree is balanced
    def isBalanced(self, root):
        if root is None: return True

        heightDiff = self.getHeight(self,root.left) - self.getHeight(self,root.right)

        if heightDiff > 1:
            return False
        else:
            return self.isBalanced(self,root.left) and self.isBalanced(self,root.right)

    def getHeight(self, root):
        if root is None: return -1

        return max(self.getHeight(self,root.left), self.getHeight(self,root.right)) + 1

    # Check if a binary tree is a valid BST
    def isValidBST(self, root):
        return self.isBST(self,root,None,None)

    def isBST(self, root, min, max):
        if root is None: return True

        if (min != None and root.data<min) or (max != None and root.data>max):
            return False

        if (not self.isBST(self, root.left, min, root.data)) or (not self.isBST(self, root.right, root.data, max)):
            return False

        return True 

    # Algo to find next in-order successor of any given node in a BST
    def findSuccessor(self, node):
        if node == None:
            return None
        
        if node.right != None: # if right subtree is not null, find leftmost node
            temp = node.right
            while (temp.left):
                temp = temp.left
            return temp

        else:
            if node.parent.data > node.data: # go up one level
                return node.parent
            else:
                if node.parent.parent.data > node.data: # go up two levels
                    return node.parent.parent
                else:
                    return node # highest possible in tree

        

