class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None #left sub-tree
    self.right = None #right sub_tree

  """adds the input value to the binary search tree, adhering
  to the rules of the ordering of elements in a binary search tree.
  """
  def insert(self, value):
    pass

  """searches the binary search tree for the input value, returning a boolean
  indicating whether the value exists in the tree or not.
  """
  def contains(self, target):
    pass

  """returns the maximum value in the binary search tree
  """
  def get_max(self):
    pass

  """
  performs a traversal of every node in the tree, executing the passed-in callback
  function on each tree node value. There is a myriad of ways to perform tree
  traversal; in this case any of them should work.
  """
  def for_each(self, cb):
    pass