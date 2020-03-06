# Implement a FIFO animal shelter that only has dogs and cats. Methods are enqueue, dequeueAny, dequeueDog, dequeueCat

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.order = 0

    def enqueue(self,data):
        if 'C' in data:
            self.cats.append((data,self.order))
            self.order += 1
        else:
            self.dogs.append((data,self.order))
            self.order += 1
    
    def dequeueAny(self):
        if not self.cats and not self.dogs:
            return None
        if not self.dogs:
            cat = self.cats.pop(0)
            return cat[0]
        if not self.cats:
            dog = self.dogs.pop(0)
            return dog[0]
        cat = self.cats[0]
        dog = self.dogs[0]
        if cat[1] < dog[1]:
            self.cats.pop(0)
            return cat[0]
        else:
            self.dogs.pop(0)
            return dog[0]

    def dequeueDog(self):
        if self.dogs:
            dog = self.dogs.pop(0)
            return dog[0]
        else:
            return None
    
    def dequeueCat(self):
        if self.cats:
            cat = self.cats.pop(0)
            return cat[0]
        else:
            return None