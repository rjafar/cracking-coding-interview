import pytest
from rotateMatrix import rotateMatrix

def test_1():
    matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    result = rotateMatrix(matrix)
    assert result == [[7,4,1],
                    [8,5,2],
                    [9,6,3]]

def test_2():
    matrix = [[1,2],
            [3,4]]
    result = rotateMatrix(matrix)
    assert result == [[3,1],
                    [4,2]]

def test_3():
    matrix = [1]
    result = rotateMatrix(matrix)
    assert result == [1]

