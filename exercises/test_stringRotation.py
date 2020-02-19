import pytest
from stringRotation import isRotation

def test_diffSizes():
    result = isRotation("hello", "hellos")
    assert result == False

def test_True():
    result = isRotation("waterbottle", "bottlewater")
    assert result == True
    result = isRotation("hello", "lohel")
    assert result == True
    result = isRotation("hi there", "therehi ")
    assert result == True

def test_False():
    result = isRotation("shello", "hesllo")
    assert result == False
    result = isRotation("water", "wateR")
    assert result == False