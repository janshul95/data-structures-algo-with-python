class Node:
    """ 
    A singly-linked node. 
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a new data node to singly linked list
        """
        # create a new node
        node = Node(data)

        # check if list is empty, if yes then update the head
        if self.head == None:
            self.head = node
        else:
            # traverse till the last node and update the next pointer of last node
            current = self.head
            while current.next:
                current = current.next
            current.next = node
