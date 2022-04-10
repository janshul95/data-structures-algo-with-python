class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next=self.top
            self.top = new_node
        self.count+=1

    def pop(self,data):
        if self.top:
            val = self.top.data
            self.top=self.top.next
            return val
        else:
            return None
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None