class Node:
    """ A singly-linked list node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularlyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """Append a new data node to circularly linked list """
        # create a new node
        new_node = Node(data)

        # check if list is empty, if yes then update the head
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self.count += 1

    def iter(self):
        """Iterate through the list"""
        current = self.head
        counter = 0
        while current:
            if counter == self.count:
                break
            val = current.data
            current = current.next
            counter += 1
            yield val

    def print(self):
        """traverse and print the linked list"""
        print("----------------CLL---------------")
        for i in self.iter():
            print(i)

    def delete(self, data):
        "delete an element from the circularly linked list"
        prev = self.head
        current = self.head
        while current == prev or prev != self.tail:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                self.count -= 1
                break
            prev = current
            current = current.next

    def contain(self, data):
        """search an element in the linked list"""
        curr = self.head
        for node in self.iter():
            if node == data:
                return True
            curr = curr.next
        return False

    def clear(self):
        """clear the entire list"""
        self.head = None
        self.tail = None
        self.count = 0
