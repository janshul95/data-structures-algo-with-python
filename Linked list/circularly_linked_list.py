class Node:
    """ A singly-linked node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def _str_ (self):
        return str(self.data)


class CircularlyLinkedList:
    def __init__(self):
        self.tail = None
        self.count = 0

    def append(self, data):
        """Append a new data node to singly linked list """
        pass

    def iter(self):
        """Iterate through the list"""
        pass

    def traverse(self):
        """traverse and print the linked list"""
        pass

    def delete(self, data):
        "delete an element from the linked list"
        pass

    def search(self,data):
        """search an element in the linked list"""
        pass