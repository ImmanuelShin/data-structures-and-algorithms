import pytest
from code_challenges.stack_and_queue.stack_queue import Stack, Queue, Node

def test_push_one():
  stack = Stack()
  stack.push("apples")
  actual = stack.pop()
  expected = "apples"
  assert actual == expected

def test_push_two():
  stack = Stack()
  stack.push("apples")
  stack.push("bananas")

  actual = stack.pop()
  expected = "bananas"
  assert actual == expected

  actual = stack.pop()
  expected = "apples"
  assert actual == expected

def test_peek_stack():
  stack = Stack()
  stack.push("apples")
  stack.push("bananas")

  actual = stack.peek()
  expected = "bananas"
  assert actual == expected

def test_empty_stack():
  stack = Stack()
  stack.push("apples")
  stack.push("bananas")
  stack.push("oranges")
  stack.pop()
  stack.pop()
  stack.pop()

  actual = stack.is_empty()
  expected = True
  assert actual == expected

def test_peek_error_stack():
  stack = Stack()
  with pytest.raises(Exception):
    stack.peek()

def test_pop_error_stack():
  stack = Stack()
  with pytest.raises(Exception):
    stack.pop()

def test_enqueue_one():
  queue = Queue()
  queue.enqueue("apples")
  actual = queue.dequeue()
  expected = "apples"
  assert actual == expected

def test_enqueue_two():
  queue = Queue()
  queue.enqueue("apples")
  queue.enqueue("bananas")

  actual = queue.dequeue()
  expected = "apples"
  assert actual == expected

  actual = queue.dequeue()
  expected = "bananas"
  assert actual == expected

def test_peek_queue():
  queue = Queue()
  queue.enqueue("First")
  queue.enqueue("Second")

  actual = queue.peek()
  expected = "First"
  assert actual == expected

def test_empty_queue():
  queue = Queue()
  queue.enqueue("First")
  queue.enqueue("Second")
  queue.enqueue("Third")

  queue.dequeue()
  queue.dequeue()
  queue.dequeue()

  actual = queue.is_empty()
  expected = True
  assert actual == expected

def test_peek_error_queue():
  queue = Queue()
  with pytest.raises(Exception):
    queue.peek()

def test_dequeue_error_queue():
  queue = Queue()
  with pytest.raises(IndexError):
    queue.dequeue()