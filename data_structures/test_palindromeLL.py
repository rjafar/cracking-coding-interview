import pytest
from linkedList import LinkedList
from palindromeLL import isLLPalindrome

def test_odd_palindrome():
    LL = LinkedList()
    LL.insert('m')
    LL.insert('o')
    LL.insert('m')
    assert True == isLLPalindrome(LL)

    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(1)
    LL.insert(2)
    LL.insert(1)
    assert True == isLLPalindrome(LL)

def test_even_palindrome():
    LL = LinkedList()
    LL.insert('m')
    LL.insert('o')
    LL.insert('o')
    LL.insert('m')
    assert True == isLLPalindrome(LL)

    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(1)
    LL.insert(1)
    LL.insert(2)
    LL.insert(1)
    assert True == isLLPalindrome(LL)

def test_not_palindrome():
    LL = LinkedList()
    LL.insert('m')
    LL.insert('o')
    LL.insert('i')
    LL.insert('m')
    assert False == isLLPalindrome(LL)

    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(1)
    LL.insert(3)
    LL.insert(2)
    LL.insert(1)
    assert False == isLLPalindrome(LL)