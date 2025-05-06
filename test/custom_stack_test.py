import pytest
from src.custom_stack_class import *

def test_push_and_top():
    stack = CustomStack(3)
    stack.push(10)
    assert not stack.is_empty()
    assert stack.top() == 10
    assert stack.size() == 1

def test_pop_element():
    stack = CustomStack(2)
    stack.push(1)
    assert stack.pop() == 1
    assert stack.is_empty()

def test_stack_full_exception():
    stack = CustomStack(1)
    stack.push(1)
    with pytest.raises(StackFullException):
        stack.push(2)

def test_stack_empty_exception_on_pop():
    stack = CustomStack(2)
    with pytest.raises(StackEmptyException):
        stack.pop()

def test_stack_empty_exception_on_top():
    stack = CustomStack(2)
    with pytest.raises(StackEmptyException):
        stack.top()
