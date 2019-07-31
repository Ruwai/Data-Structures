class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        return self.left.insert(value)

    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        return self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True

    if target < self.value:
      if not self.left:
        return False
      elif target == self.value:
        return True
      else:
        return self.left.contains(target)

    if target > self.value:
      if not self.right:
        return False
      elif target == self.value:
        return True
      else:
        return self.right.contains(target)

  def get_max(self):
    right_branch = self.value if self.right is None else self.right.get_max()

    return max(self.value, right_branch)

  def for_each(self, cb):
    cb(self.value)

    if self.left:
      self.left.for_each(cb)

    if self.right:
      self.right.for_each(cb)