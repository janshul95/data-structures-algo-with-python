class Node:
    """ A doubly-linked list node. """

    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """Append a new data node to singly linked list """
        new_node = Node(data)  # create a new node
        if self.head is None:  # if list is empty
            self.head = new_node
            self.tail = new_node
        else:  # append at the tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.count += 1

    def iter(self):
        """Iterate through the list"""
        # is a generator which gives the data value of current node
        curr = self.head
        while curr:
            val = curr.data
            curr = curr.next
            yield val

    def delete(self, data):
        """delete an element from the linked list"""

        node_deleted = False

        # case 1: list is empty
        if self.head is None:
            node_deleted = False

        # case 2: data is at head, move the head to next node
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            node_deleted = True

        # case 3: data is at tail, move the tail to previous node
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        # Case 4 data is between head and tail
        else:
            curr = self.head
            while curr:
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    node_deleted = True

                curr = curr.next

        if node_deleted:
            self.count -= 1

    def print(self):
        """traverse and print the linked list"""
        print("-----------DLL-----------")
        for node in self.iter():
            print(node)

    def contain(self, data):
        """search an element in the linked list"""
        for node_data in self.iter():
            if node_data == data:
                return True

        return False
