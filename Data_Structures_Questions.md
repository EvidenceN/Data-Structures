Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
O(n)

2. What is the runtime complexity of `push` using a linked list?

3. What is the runtime complexity of `pop` using a list?

4. What is the runtime complexity of `pop` using a linked list?

5. What is the runtime complexity of `len` using a list?

6. What is the runtime complexity of `len` using a linked list?

## Queue

1. What is the runtime complexity of `enqueue` using a list?

2. What is the runtime complexity of `enqueue` using a linked list?

3. What is the runtime complexity of `dequeue` using a list?

4. What is the runtime complexity of `dequeue` using a linked list?

5. What is the runtime complexity of `len` using a list?

6. What is the runtime complexity of `len` using a linked list?

for linked list, appending values to the head is O(1) performance

for linked list, removing values from the tail is O(1) performance

For lists, appending values to the head is O(n) operation because values have to shift right in order for something to be added to the head. 

For lists, removing values from the head is O(n) operation because all values have to shift left after the 0-index value is popped off. 

For stacks = last in, first out

Linked list = adding to tail = O(1) operation
Linked list = removing from tail = O(1) operation

Regular list = appending to end of list = 0(1) operation. 
Regular list = removing from end of list is 0(1) operation

For queues = first in, first out

Linked list = adding to the tail = O(1) operation. 
        REmoving from the head = 0(1) operation


Regular list = adding to tail = O(1) operation
        removing from the head = O(n)

From this website https://docs.python.org/2/library/collections.html#collections.deque

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.



## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
