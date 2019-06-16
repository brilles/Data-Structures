class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  """adds the input value to the binary search tree, adhering
  to the rules of the ordering of elements in a binary search tree.
  """
  def insert(self, value):
    # 0. wrap the value in a node
    # 1. Compare the element against the current node's value
    # 2. based on the result of the comparison, go left or right
    # 3. IF we find an empty spot, park the value there
    # 4. Otherwise, go back to step 1

    # what is the base case?
    # base case: we've found an empty spot where we can add the value
    if value < self.value:
      # we go left
      # if there is no child, park this node here
      if not self.left:
        self.left = BinarySearchTree(value)
      # recurse on the left child
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  """searches the binary search tree for the input value, returning a boolean
  indicating whether the value exists in the tree or not.
  """
  def contains(self, target):
    # 1. compare the current node's value
    # 2. based in the result of the comparison, return true or go left or right and call contains again on that subtree
    if target == self.value:
      return True 
    elif target < self.value:
      if self.left:
        if self.left.value == target:
          return True
        else: 
          return self.left.contains(target)
    elif target >= self.value:
      if self.right:
        if self.right.value == target:
          return True
        else:
          return self.right.contains(target)
    else: 
      return False

  """returns the maximum value in the binary search tree
  """
  def get_max(self):
    max_value = self.value
    while True: 
      if self.value > max_value:
        max_value: self.value
      if self.right: 
        if self.right.value > max_value:
          max_value = self.right
          return self.right.get_max()
      if self.left and not self.right: 
        if self.left > max_value:
          max_value = self.left.value
          return self.left.get_max()
      else: 
        break
    return max_value
    

  """
  performs a traversal of every node in the tree, executing the passed-in callback
  function on each tree node value. There is a myriad of ways to perform tree
  traversal; in this case any of them should work.
  """
  def for_each(self, cb):
    cb(self.value) 
    if self.right:
      self.right.for_each(cb)
    if self.left:
      self.left.for_each(cb)