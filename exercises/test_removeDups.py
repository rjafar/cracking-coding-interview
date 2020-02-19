import pytest
from removeDups import removeDups

def test_noDups():
    ll = [1,2,3]
    assert ll == removeDups(ll)

def test_removeDups():
    ll = [1,2,1]
    assert [1,2] == removeDups(ll)
    ll = [1,1,1,1,1]
    assert [1] == removeDups(ll)
    ll = [1,1,3,2,3,1,2]
    assert [1,3,2] == removeDups(ll)

def test_empty():
    ll = []
    assert [] == removeDups(ll)


