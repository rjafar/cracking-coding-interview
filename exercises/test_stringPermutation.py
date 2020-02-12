import pytest
from stringPermutation import isPermutation

    
def test_true():
    result = isPermutation("hola", "hloa")
    assert result == True, "Should be True"
    result = isPermutation("What's up?", " '?hatWpus")
    assert result == True, "Should be True"
    result = isPermutation("@#!", "!@#")
    assert result == True, "Should be True"

def test_false():
    result = isPermutation("", " ")
    assert result == False, "Should be False"
    result = isPermutation("abc", "aabc")
    assert result == False, "Should be False"
    result = isPermutation("#?#", "?#?")
    assert result == False, "Should be False"
