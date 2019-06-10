class Heap:
  def __init__(self):
    self.storage = []

  """adds the input value into the heap; this method should ensure
  that the inserted value is in the correct spot in the heap
  """
  def insert(self, value):
    pass

  """removes and returns the 'topmost' value from the heap; this method
  needs to ensure that the heap property is maintained after the topmost
  element has been removed
  """
  def delete(self):
    pass

  """returns the maximum value in the heap in constant time
  """
  def get_max(self):
    pass

  """returns the number of elements stored in the heap
  """
  def get_size(self):
    pass

  """moves the element at the specified index 'up' the heap by swapping it
  with its parent if the parent's vaule is less than the value at the spefified index.
  """
  def _bubble_up(self, index):
    pass

  """grabs the indices of this element's children and determines which child has a 
  larger value. If the larger child's value is larger than the parent's value, the 
  child element is swapped with the parent.
  """
  def _sift_down(self, index):
    pass
