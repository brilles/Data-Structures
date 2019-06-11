"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is pointing to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  """replaces the head of the list with a new value that 
  is passed in.
  """
  def add_to_head(self, value):
    new_node = ListNode(value)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      old_head = self.head
      old_head.insert_before(value)
      self.head = old_head.prev
    self.length += 1

  """removes the head node and returns the value stored 
  in it.
  """
  def remove_from_head(self):
    if not self.head and not self.tail:
      return None
    if self.head is self.tail:
      old_head = self.head
      self.head = None
      self.tail = None
      self.length -= 1
      return old_head.value

    old_head = self.head
    self.head.delete()
    self.length -= 1
    return old_head.value

  """replaces the tail of the list with a new value that 
  is passed in
  """
  def add_to_tail(self, value):
    new_node = ListNode(value)
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      old_tail = self.tail
      old_tail.insert_after(value)
      self.tail = old_tail.next
    self.length += 1

  """ removes the tail node and returns the value stored 
  in it.
  """
  def remove_from_tail(self):
    if not self.head and not self.tail:
      return None
    if self.head is self.tail:
      old_tail = self.tail
      self.head = None
      self.tail = None
      self.length -= 1
      return old_tail.value
    
    old_tail = self.tail
    self.tail.delete()
    self.length -= 1
    return old_tail.value

  """ takes a reference to a node in the list and moves
  it to the front of the list, shifting all other list 
  node down
  """
  def move_to_front(self, node):
    moving_node = node
    self.delete(node)
    self.add_to_head(moving_node.value)

  """ takes a reference to a node in the list and moves 
  it to the end of the list, shifting all other list nodes
  up
  """
  def move_to_end(self, node):
    moving_node2 = node
    self.delete(node)
    self.add_to_tail(moving_node2.value)

  """ takes a reference to a node in the list and removes
  it from the list. The deleted node's previous and next 
  pointers should point to each afterwards.
  """
  def delete(self, node): 
    node_to_delete = node
    if node is self.head:
      self.head = node_to_delete.next
    if node is self.tail:
      self.tail = node_to_delete.prev
    node.delete()
    self.length -= 1


  """returns the maximum value in the list
  """
  def get_max(self):
    if not self.head and not self.tail:
      return None
    current = self.head
    greatest = self.head
    while current:
      if current.value >= greatest.value:
        greatest = current
      current = current.next
    return greatest.value
