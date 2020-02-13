import pytest
from compressString import compress

def test_empty():
    result = compress(" ")
    assert result == " "
    result = compress("   ")
    assert result == " 3"

def test_orig():
    result = compress("abc")
    assert result == "abc"
    result = compress("abbc d")
    assert result == "abbc d"

def rest_compress():
    result = compress("aabbbbcc")
    assert result == "a2b4c3"
    result = compress("aaa   bbbbb  ")
    assert result == "a3 3b5 2"