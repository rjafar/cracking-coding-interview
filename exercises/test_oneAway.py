import pytest
from oneAway import isOneAway

def test_true():
    result = isOneAway("abc", "abd")
    assert result == True
    result = isOneAway("ab", "abc")
    assert result == True
    result = isOneAway("abc", "ab")
    assert result == True

def test_false():
    result = isOneAway("abc", "acd")
    assert result == False
    result = isOneAway("ab", "abcc")
    assert result == False
    result = isOneAway("abc", "a")
    assert result == False

def test_empty():
    result = isOneAway("", "a")
    assert result == True
    result = isOneAway("", "abc")
    assert result == False
    result = isOneAway("abc", "")
    assert result == False
    result = isOneAway("a", "")
    assert result == True