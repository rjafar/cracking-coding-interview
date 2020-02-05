import pytest
from memoization_fibonacci import fib

    
def test_fib_zero():
    result = fib(0)
    assert result[0] == 0, "Should be 0, got " + result[0]

def test_one():
    result = fib(1)
    assert result[1] == 1, "Should be 1, got " + result[1]

def test_ten():
    result = []
    for i in range(11):
        result = fib(i)
    assert result[0] == 0, "Should be 0, got " + result[0]
    assert result[1] == 1, "Should be 1, got " + result[1]
    assert result[2] == 1, "Should be 1, got " + result[2]
    assert result[3] == 2, "Should be 2, got " + result[3]
    assert result[4] == 3, "Should be 3, got " + result[4]
    assert result[5] == 5, "Should be 5, got " + result[5]
    assert result[6] == 8, "Should be 8, got " + result[6]
    assert result[7] == 13, "Should be 13, got " + result[7]
    assert result[8] == 21, "Should be 21, got " + result[8]
    assert result[9] == 34, "Should be 34, got " + result[9]
    assert result[10] == 55, "Should be 55, got " + result[10]

        