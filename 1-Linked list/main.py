from singly_linked_list import SinglyLinkedList
from doubly_linked_list import DoublyLinkedList
from circularly_linked_list import CircularlyLinkedList


def print_LL(LL):
    head = LL.head
    while head:
        print(head.data)
        head = head.next


def main():

    # books = SinglyLinkedList()
    # books = DoublyLinkedList()
    books = CircularlyLinkedList()
    books.append("book 1")
    books.append("book 2")
    books.append("book 3")
    books.append("book 4")
    books.print()
    books.delete("book 1")
    books.print()
    print(books.contain("book 1"))


if __name__ == "__main__":
    main()
