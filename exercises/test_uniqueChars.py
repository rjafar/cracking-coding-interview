import pytest
from uniqueChars import isUnique

    
def test_unique():
    result = isUnique("hola")
    assert result == True, "Should be True"
    result = isUnique("What's up?")
    assert result == True, "Should be True"

def test_notUnique():
    result = isUnique("Hello")
    assert result == False, "Should be False"
    result = isUnique("  ")
    assert result == False, "Should be False"
    result = isUnique("Hi how are you?")
    assert result == False, "Should be False"

def test_upperLower():
    result = isUnique("hH")
    assert result == True, "Should be True"
    result = isUnique("iI")
    assert result == True, "Should be True"

def test_special():
    result = isUnique("11")
    assert result == False, "Should be False"
    result = isUnique("12@&")
    assert result == True, "Should be True"