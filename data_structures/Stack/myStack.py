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
        return self.stack[0]

    def sort(self):
        s2 = MyStack()
        while (self.size()!=0):
            temp = self.pop()
            if s2.size()!=0:
                if temp > s2.peek():
                    self.push(s2.pop())
            s2.push(temp)
        for i in range(s2.size()):
            self.push(s2.pop())

