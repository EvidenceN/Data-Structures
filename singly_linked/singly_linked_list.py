class Node:
    """
    A node has only 2 things. A value, and a next
    node location

    Default behaviour is none
    """
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        """
        We need to be able to get the value from the node

        """
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        """
        Being able to set the next node
        """
        self.next_node = new_next



class LinkedList:
    """
    made up of nodes
    at the linked list level, 
    we need head and tail
    """

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_tail(self, value):
        """
        Being able to add to the tail of the linked list
        """
        new_node = Node(value, None)

        # adding to the tail of an empty linked list
        # check if there is no head

        if not self.head:
            # if there is no head, add new node
            self.head = new_node
            self.tail = new_node
        else:
            # if the linked list is not empty
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        """
        When we need to remove the head
        """
        # check if linked list is empty/no head
        if not self.head:
            return None

        # check if head has no next value, that means there is 
        # a single element in the linked list


        if not self.head.get_next():
            head = self.head
            self.head = None
            self.head = None
            return head.get_value()

        # check to see if there are more than one item in the linked list

        value = self.head.get_value()
        # set the head reference to the current head's next node in the list

        self.head = self.head.get_next()
        return value

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at;
        # update this as we traverse 
        current = self.head

        # check to see if we're at a valid node

        while current:
            # return True if the current value we're looking at matches out target value
            if current.get_value() == value:
                return True
            # update our current node t the current node's next node
            current = current.get_next()

        # if we've gotten here ,then the target node isn't in our list
        return False
        