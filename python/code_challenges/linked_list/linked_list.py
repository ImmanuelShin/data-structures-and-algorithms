class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
  
  def __str__(self):
    return str(self.data)
        
class Linked_List:
  def __init__(self):
    self.head = None
      
  def insert(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next

    current.next = new_node
  
  def includes(self, data):
    if self.head is None:
      return False
    else:
      i = self.head
      while i is not None:
        if i.data == data:
            return True
        i = i.next
      return False
          
  def to_string(self):
    res = ""
    node = self.head
    
    while node:
      res += "{ " + str(node.data) + " }"
      if node.next is None:
        res += " -> NULL"
      else:
        res += " -> "
      node = node.next
    return res
  
  def is_empty(self):
    return self.head == None
  
  def append(self, data):
    if self.head == None:
      self.insert(data)
    else:
      node = self.head
      while node.next is not None:
        node = node.next
      node.next = Node(data)
  
  def insert_before(self, value, data):
    if self.is_empty():
        raise Exception("List is empty")

    if self.head.data == value:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    node = self.head
    while node.next is not None:
        if node.next.data == value:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            return
        node = node.next

    raise Exception("Value not found in list")
  
  def insert_after(self, value, data):
    if self.is_empty():
      raise Exception("List is empty")

    node = self.head
    while node:
      if node.data == value:
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
        return
      node = node.next
    raise Exception("Value not found in list")
  
  def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

  def kth_from_end(self, k):
    if k < 0:
      raise IndexError("Invalid Negative Value")
    scout = army = self.head

    for _ in range(k+1):
      if scout is None:
        raise IndexError("K is greater than list length")
      scout = scout.next

    while scout:
      army = army.next
      scout = scout.next

    return army.data
  
  def __str__(self):
    return self.to_string()