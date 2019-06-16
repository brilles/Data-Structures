class Heap:
  def __init__(self):
    self.storage = []

  """adds the input value into the heap; this method should ensure
  that the inserted value is in the correct spot in the heap
  """
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  """removes and returns the 'topmost' value from the heap; this method
  needs to ensure that the heap property is maintained after the topmost
  element has been removed
  """
  # TODO
  def delete(self):
    topmost_value = self.storage.pop(0)
    self._sift_down(0)
    self._bubble_up(len(self.storage) - 1)
    self._bubble_up(len(self.storage) - 2)
    self._bubble_up(len(self.storage) - 3)
    self._bubble_up(len(self.storage) - 4)
    return topmost_value

  """returns the maximum value in the heap in constant time
  """
  def get_max(self):
    return self.storage[0]


  """returns the number of elements stored in the heap
  """
  def get_size(self):
    return len(self.storage)

  """moves the element at the specified index 'up' the heap by swapping it
  with its parent if the parent's vaule is less than the value at the spefified index.
  """
  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else: 
        break

  """grabs the indices of this element's children and determines which child has a 
  larger value. If the larger child's value is larger than the parent's value, the 
  child element is swapped with the parent.
  """
  
  def _sift_down(self, index):
    while index > 0:
      left_child_index = 2*index + 1
      right_child_index = 2*index + 2

      if left_child_index <= self.get_size() and right_child_index <= self.get_size():
        if self.storage[left_child_index] >= self.storage[rightChild]:
          if self.storage[left_child_index] > self.storage[index]:
            self.storage[index], self.storage[left_child_index] = self.storage[left_child_index], self.storage[index]
        else:
          if self.storage[right_child_index] > self.storage[index]:
            self.storage[index], self.storage[right_child_index] = self.storage[right_child_index], self.storage[index]

      if left_child_index <= self.get_size():
        if self.storage[left_child_index] > self.storage[index]:
          self.storage[index], self.storage[left_child_index] = self.storage[left_child_index], self.storage[index]

      if right_child_index <= self.get_size():
        if self.storage[right_child_index] > self.storage[index]:
          elf.storage[index], self.storage[right_child_index] = self.storage[right_child_index], self.storage[index]
      
      else: 
        break


