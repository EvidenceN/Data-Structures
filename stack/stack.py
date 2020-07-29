"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

* Should have the methods: `push`, `pop`, and `len`.
   * `push` adds an item to the top of the stack.
   * `pop` removes and returns the element at the top of the stack
   * `len` returns the number of elements in the stack.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

PYTHON EXAMPLE https://docs.python.org/2/tutorial/datastructures.html
"""

# Using an ARRAY to do stack
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        return self.storage.pop()

import sys

#sys.path.insert(1,r"C:\Users\Samsung\Google Drive (evidencen@evidencen.com)\Data Science Lambda\Unit 5_Computer Science\2 data structures\Data-Structure")

sys.path.append('../')

from singly_linked.singly_linked_list import LinkedList, Node

# Using an a "linked list" to do stack
linked = LinkedList()
node = Node()
class Stacklink:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # get the length of the linked list
        return len(self.storage)

    def push(self, value):
        # add the value to the tail
        return self.storage.add_to_tail(value)

    def pop(self):
        # first get the value of the current tail
        value = node.get_value()
        next_tail = node.set_next(value)