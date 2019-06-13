class Heap:
  def __init__(self):
    self.storage = []

  """adds the input value into the heap; this method should ensure
  that the inserted value is in the correct spot in the heap
  """
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)
    print(self.storage)

  """removes and returns the 'topmost' value from the heap; this method
  needs to ensure that the heap property is maintained after the topmost
  element has been removed
  """
  def delete(self):
    # deleted = self.storage[0]
    pass 

  """returns the maximum value in the heap in constant time
  """
  def get_max(self):
    if self.storage[0]:
      return self.storage[0]
    else: 
      return None

  """returns the number of elements stored in the heap
  """
  def get_size(self):
    pass
    # size = len(self.storage)
    # return size

  """moves the element at the specified index 'up' the heap by swapping it
  with its parent if the parent's vaule is less than the value at the spefified index.
  """
  def _bubble_up(self, index):
    # keep bubbling up unitl we've either reached the top of the heap
    # or we've reached a point where the parent is higher priority
    # on a single bubble_up iteration
    # get the parent index
    # compare the child against the value of the parent
    # if the child'd value is higher priority than its parent value
      # swap them
      # update index
    # child is a a valid spot
    # stop bubbling up

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
    pass
