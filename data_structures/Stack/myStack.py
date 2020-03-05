# Implementation of Stack using python built-in list

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.insert(0,data)
        return data

    def pop(self):
        return self.stack.pop(0)

    def isEmpty(self):
        return self.stack == []
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if not len(self.stack):
            return self.stack[0]
        return None
