from src.custom_stack_class import CustomStack, StackEmptyException

class NumberAscOrder:
    def sort(self, stack: CustomStack) -> list:
        if stack.is_empty():
            return []
        
        sorted_list = []
        while not stack.is_empty():
            sorted_list.append(stack.pop())
        
        return sorted(sorted_list)
