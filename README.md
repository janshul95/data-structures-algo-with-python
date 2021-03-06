# data-structures-algo-with-python
Data Structures and Algorithms implementation using python

## Arrays
- Array is a sequential list of data. Being sequential means that each element is stored right after the previous on in memory
- If your array is really big and you are low on memory than it could be impossible to find large enpugh storage to fit your entire array
- Flip side of the coin is that arrays are very fast.
- Since each element is stored sequentially in continuous memory location. Each element of array can be accessed in O(1) time 
- There is no need to jump around b/w different memory locations
- This could be **a very important point to take into consideration when choosing a list or an array** for your real world application

## Pointer structures
- Contrary to arrays, pointer structures are list of items that can be spread out in memory.
- This is beacause each item contains one or more links (pointer) to other items in the structure
- The types of links can vary based on the type of data structures we have 
    - an item in linked list  will have links to next or previous item
    - in case of tree, we have parent-chiled as well as sibling links

## Nodes
- At the heart of lists and several other data structures is the concept of a node
- We can think of a node as a container, which consists of data and links to other nodes  

Note: A link is a pointer

A simple node implementation  

        class Node:  
            def __init__ (self,data=None):
                self.data = data  
                self.next = None

One thing you may also want to do is to implement _str_ method so that if required, you can easily print the node  

            def _str_ (self):
                return str(self.data)

Now using variations of the node class we can implement almost all the data structures

1. [Linked list](./Linked%20list/)
2. [Stacks](./2-Stacks/)
3. [Queues](./3-Queues/)
4. [Trees](./4-Trees/)
5. [Heaps](./5-Heaps/)
6. [Graph](./6-Graph/)
