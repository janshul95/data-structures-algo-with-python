from singly_linked_list import SinglyLinkedList


def print_LL(LL):
    head = LL.head
    while head:
        print(head.data)
        head = head.next

def main():      

    books = SinglyLinkedList()
    books.append("book 1")
    books.append("book 2")
    books.append("book 3")
    books.append("book 4")
    books.traverse()
    books.delete("book 3")
    books.traverse()
    print(books.search("book 4"))


if __name__ == "__main__":
    main()