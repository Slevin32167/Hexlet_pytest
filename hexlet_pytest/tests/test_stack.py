import pytest


def test_stack_basic():
    stack = []
    stack.append("one")
    stack.append("two")
    assert stack.pop() == "two"
    assert stack.pop() == "one"


def test_stack_emptiness():
    stack = []
    assert not stack
    stack.append("one")
    assert bool(stack)
    stack.pop()
    assert not stack


def test_stack_empty_pop():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
