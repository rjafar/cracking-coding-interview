import pytest
from zeroMatrix import zeroMatrix

def test_nozero():
    matrix = [[5,2],
            [3,1],
            [4,5]]
    result = zeroMatrix(matrix) 
    assert result == [[5,2],
                    [3,1],
                    [4,5]]

def test_onezero():
    matrix = [[5,2],
            [3,0],
            [4,5]]
    result = zeroMatrix(matrix) 
    assert result == [[5,0],
                    [0,0],
                    [4,0]]

def test_multzero():
    matrix = [[0,2],
            [3,1],
            [0,5]]
    result = zeroMatrix(matrix) 
    assert result == [[0,0],
                    [0,1],
                    [0,0]]
                
    matrix = [[5,0],
            [3,0]]
    result = zeroMatrix(matrix) 
    assert result == [[0,0],
                    [0,0]]