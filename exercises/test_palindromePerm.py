import pytest
from palindromePerm import isPalindromePerm

def test_true():
    result = isPalindromePerm("tact coa")
    assert result == True
    result = isPalindromePerm("tact coatt")
    assert result == True
    result = isPalindromePerm("hi ho oi")
    assert result == True

def test_false():
    result = isPalindromePerm("tact coaz")
    assert result == False
    result = isPalindromePerm("ooooab")
    assert result == False
    result = isPalindromePerm("hi ho oilp")
    assert result == False

def test_empty():
    result = isPalindromePerm("")
    assert result == True

def test_special():
    result = isPalindromePerm(" ")
    assert result == True
    result = isPalindromePerm("-- ")
    assert result == True
    result = isPalindromePerm("?/-")
    assert result == False

def test_upperLower():
    result = isPalindromePerm("tT")
    assert result == False
