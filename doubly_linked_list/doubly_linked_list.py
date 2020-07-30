"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    """
    wrap the given value in a listnode and insert it after this node. not that this node could already have a next node it is pointing to
    """

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next 
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value, None, None)

        # check if the doubly linked list is empty

        # if head is empty, then the new node = head & tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # the new node next value is pointing to the current head
            new_node.next = self.head

            # pointing the previous head node to the new node
            self.head.prev = new_node

            # setting the new node as the current head
            self.head = new_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        # setting current to the current head
        current = self.head
        # set the next node as the new head
        self.head = current.next

        # set the previous pointer from the new head node to none instead of current
        self.head.prev = None
        self.length -= 1
        return current

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        # first create a new node
        new_node = ListNode(value, None, None)

        # if head and tail is empty

        if not self.head and not self.tail:
            # set the tail and head to the new node
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # set the previous pointer of the new node to the current tail
            new_node.prev = self.tail

            # set the next pointer from the new node to none
            new_node.next = None
            # set the next pointer from previous tail node to the new value
            self.tail.next = new_node
            # set the new node as the current tail
            self.tail = new_node
            self.length +- 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):

        # current tail
        current = self.tail

        # new tail is current tail's previous node

        self.tail = current.prev

        # set the current tail next node to none

        self.tail.next = None

        return current
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.node = node

        # I could do the proceedure below or just use the function defined above.
        # 
        # Don't fully understand the function below, so will do it manually.  

        """moved_node = ListNode(node.value)
        moved_node.insert_before(self.head.value)
"""
        current = self.head

        # before setting the previous pointer from the node being moved to none

        # need to say that the node located on the previous pointer of node being moved is now connected to the node located on the next point of node being moved. 

        # previous node on the previous pointer of what is being moved
        prev_node = self.node.prev 

        # next node on the next pointer of what is being moved

        next_node = self.node.next

        # the next pointer associated with the previous node is now pointing to the next node of what is being moved.

        prev_node.next = next_node

        # the previous pointer associated with the next node of what is being moved is now pointing to the previous pointer of what is being moved

        next_node.prev = prev_node

        # set the previous pointer from the specified node to none

        node.prev = None

        # set the previous from the current head to the new node. 

        current.prev = node

        # set the next pointer from the node being moved to the current head

        node.next = current

        self.head = node
        
    """    
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.node = node

        current = self.tail

        # previous node on the previous pointer of what is being moved
        prev_node = self.node.prev 

        # next node on the next pointer of what is being moved

        next_node = self.node.next

        # the next pointer associated with the previous node is now pointing to the next node of what is being moved.

        prev_node.next = next_node

        # the previous pointer associated with the next node of what is being moved is now pointing to the previous pointer of what is being moved

        next_node.prev = prev_node

        # set the previous pointer from the specified node to current tail

        node.prev = current

        # set the next pointer from the current tail to the new node. 

        current.next = node

        # set the next pointer from the node being moved to the None

        node.next = None

        self.tail = node
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.node = node
        if node.prev:
            node.prev.next = node.next 
        if node.next:
            node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        "Got it from this website https://www.javatpoint.com/python-program-to-find-the-maximum-and-minimum-value-node-from-a-circular-linked-list"

        current = self.head    
        #Initializing max to initial node data    
        maximum = self.head.value    
        if(self.head == None):    
            print("List is empty")    
        else:    
            while(True):    
                #If current node's data is greater than max    
                #Then replace value of max with current node's data    
                if(maximum < current.value):    
                    maximum = current.value    
                current = current.next    
                if(current == self.head):    
                    break    
        print("Maximum value node in the list: "+ str(maximum))