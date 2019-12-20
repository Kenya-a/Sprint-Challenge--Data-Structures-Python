import sys

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else: 
                self.right.insert(value)
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        while True:
            if target == self.value:
                return True
            elif target < self.value:
                if self.left == None:
                    return False
                else:
                    self = self.left
            else:
                if self.right == None:
                    return False
                else:
                    self = self.right
        

    # Return the maximum value found in the tree
    def get_max(self):
        while self.right: # loops down to find the most right leaf
            self = self.right
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)
        
