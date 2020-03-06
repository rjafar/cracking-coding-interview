import pytest
from animalShelter import AnimalShelter

def test_deqAny():
    shelter = AnimalShelter()
    shelter.enqueue("C0")
    shelter.enqueue("C1")
    shelter.enqueue("D2")
    shelter.enqueue("C3")
    shelter.enqueue("D4")
    assert "C0" == shelter.dequeueAny()
    assert "C1" == shelter.dequeueAny()

def test_deqDog():
    shelter = AnimalShelter()
    shelter.enqueue("C0")
    shelter.enqueue("C1")
    shelter.enqueue("D2")
    shelter.enqueue("C3")
    shelter.enqueue("D4")
    assert "D2" == shelter.dequeueDog()
    assert "D4" == shelter.dequeueDog()

def test_deqCat():
    shelter = AnimalShelter()
    shelter.enqueue("C0")
    shelter.enqueue("C1")
    shelter.enqueue("D2")
    shelter.enqueue("C3")
    shelter.enqueue("D4")
    assert "C0" == shelter.dequeueCat()
    assert "C1" == shelter.dequeueCat()