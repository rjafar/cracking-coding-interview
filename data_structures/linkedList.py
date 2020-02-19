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



