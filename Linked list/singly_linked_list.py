class Node:
    """ A singly-linked node. """

    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def _str_ (self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """Append a new data node to singly linked list """
        # create a new node
        node = Node(data)

        # check if list is empty, if yes then update the head
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.count +=1

    def iter(self):
        """Iterate through the list"""
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def traverse(self):
        """traverse and print the linked list"""
        print([i for i in self.iter()])

    def delete(self, data):
        "delete an element from the linked list"
        prev = self.head
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.count-=1
                break
            prev = current
            current=current.next

    def search(self,data):
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