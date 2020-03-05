# Implementation of Queue using python built-in list

class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.insert(self.size(),data)
        return data

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []
    
    def size(self):
        return len(self.queue)
