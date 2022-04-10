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

1. [Linked list](./Linked%20list/)
2. [Stacks](./Stacks/)
3. [Queues](./Queues/)
4. [Trees](./Trees/)
5. [Heaps](./Heaps)
6. [Graph](./Graph/)
