
from matplotlib.pyplot import get


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append_list(self,value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):        
        if self.length == 0 :
            print('No items to remove')
        pre = self.head
        post = self.head
        while (post.next):
            pre = post
            post = post.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return post

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def prepop(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        if self.length >= 1:
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self,index):
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
    
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_list(value)
        temp = self.get(index-1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self,index):
        if index < 0 or index > self.length :
            return None
        if index == 0:
            return self.prepop()
        if index == self.length - 1:
            return self.pop()
        removed = self.get(index)
        pre = self.get(index -1)
        pre.next = removed.next
        removed.next = None
        self.length -= 1
        return removed

    def reverse(self):
        if self.length == 1:
            return True
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True

my_linked_list = LinkedList(1)
my_linked_list.append_list(2)
my_linked_list.append_list(3)

l = my_linked_list.reverse()
my_linked_list.print_list()

