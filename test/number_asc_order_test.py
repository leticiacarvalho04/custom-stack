# test/number_asc_order_test.py
import pytest
from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder

def test_sort_with_six_random_numbers():
    stack = CustomStack(6)
    numbers = [42, 7, 29, 15, 3, 18]
    for num in numbers:
        stack.push(num)
    
    sorter = NumberAscOrder()
    result = sorter.sort(stack)

    assert result == sorted(numbers)

def test_sort_with_empty_stack():
    stack = CustomStack(6)
    sorter = NumberAscOrder()
    result = sorter.sort(stack)

    assert result == []
