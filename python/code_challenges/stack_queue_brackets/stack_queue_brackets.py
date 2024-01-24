import re
from code_challenges.stack_and_queue.stack_queue import Stack, Queue

def multi_bracket_validation(str):
    open_stack = Stack()
    for i in str:
        if i in '([{':
            open_stack.push(i)
        elif i in ')]}':
            if open_stack.is_empty():
                return False
            top = open_stack.pop()
            if not ((i == ')' and ord(top) == ord(i) - 1) or
                    (i in '}]' and ord(top) == ord(i) - 2)):
                return False
    return open_stack.is_empty()