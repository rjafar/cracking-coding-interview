import pytest
from URLify import urlify


def test_short():
    result = urlify("hi there  ", 8)
    assert result == "hi%20there"

def test_long():
    result = urlify("hello my name is Bob        ", 20)
    assert result == "hello%20my%20name%20is%20Bob"