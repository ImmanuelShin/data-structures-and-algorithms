class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next =  next

class Stack:
  def __init__(self):
    self.head = Node("head")
    self.size = 0

  def is_empty(self):
    return self.size == 0
  
  def push(self, value):
    new_node = Node(value)
    new_node.next = self.head.next
    self.head.next = new_node
    self.size += 1

  def pop(self):
    if self.is_empty():
      raise Exception("Ain't nothing here")
    remove = self.head.next
    self.head.next = self.head.next.next
    self.size -= 1
    return remove.data
  
  def peek(self):
    if self.is_empty():
      raise Exception("Nothing to see here")
    return self.head.next.data
  
class Queue:
  def __init__(self):
    self.front = None
    self.back = None

  def is_empty(self):
    return self.front is None
  
  def enqueue(self, value):
    new_node = Node(value)
    if self.back:
      self.back.next = new_node
    self.back = new_node
    if not self.front:
      self.front = new_node

  def dequeue(self):
    if self.is_empty():
      raise IndexError("There's nothing here")
    data = self.front.data
    self.front = self.front.next
    if self.front is None:
      self.back = None
    return data
  
  def peek(self):
    if self.is_empty():
      raise Exception("Nothing to see here")
    return self.front.data
