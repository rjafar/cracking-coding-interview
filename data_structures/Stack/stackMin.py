# Implements a method to find the min element in an unsorted stack
# Time Complexity: O(1)

from myStack import MyStack

class StackMin:
    def __init__(self):
        self.sMin = MyStack()

    def push(self,data):
        if data < self.min():
            self.sMin.push(data)
        self.push(data)

    def pop(self):
        val = self.pop()
        if val == self.sMin.min():
            self.sMin.pop()
        return val

    def min(self):
        return self.sMin.peek()
 