class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        temp = self.tail
        temp.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        new_node.prev = temp
        self.length += 1
        return True

    def pop(self):
        last = self.tail
        prev = last.prev
        self.tail = prev
        prev.next = None

mydll = DoublyLinkedList(7)
mydll.append(10)
mydll.append(3)
mydll.print_list()