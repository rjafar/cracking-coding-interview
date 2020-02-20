# Implementation of singly linked linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = newNode
        else:
            self.head = newNode

    def remove(self, data):
        curr = self.head
        if curr.data == data:
            self.head = curr.next
            curr = None
        else:
            while (curr.next):
                if curr.next.data == data:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
    
    def find(self, data):
        curr = self.head
        while (curr):
            if curr.data == data:
                return curr.data
            else:
                curr = curr.next

    def size(self):
        count = 0
        curr = self.head
        while (curr):
            count += 1
            curr = curr.next
        return count

    def printLinkedList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next

    # function that returns the linked list with duplicates removed
    def removeDups(self):
        m = {}
        prev = None
        curr = self.head
        while(curr):
            if curr.data not in m:
                m[curr.data] = 1
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        return self

    # function that returns kth to last element in the linked list
    def kthToLast(self,k):
        n = self.size()
        if k >= 0 | k > n: return None
        kth = n - k
        curr = self.head
        for i in range(kth+1):
            temp = curr.data
            curr = curr.next
        return temp
 

