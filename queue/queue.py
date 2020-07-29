"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

PYTHON EXAMPLE https://docs.python.org/2/tutorial/datastructures.html
"""

#Queue using ARRAY as storage

"""
Why I used deque
It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

"""
from collections import deque

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = deque([])
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.append(value)

    def dequeue(self):
        return self.storage.popleft()

import sys
sys.path.append('../')

from singly_linked.singly_linked_list import LinkedList, Node

# implementing queue using linked list
# Using an a "linked list" to do stack

linked = LinkedList()
node = Node()
class Queuelink:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # get the length of the linked list
        return len(self.storage)

    def enque(self, value):
        # add the value to the head
        node = Node()
        return node.set_next(value)

    def dequeue(self):
        # Dequeing first item would be removing the head
        return self.storage.remove_head()