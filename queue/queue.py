class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Queue():
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_q(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        temp = self.first
        if self.first is None:
            return None
        self.first = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.last = None
            self.first = None
        return temp.value


myq = Queue(4)
myq.enqueue(3)
myq.dequeue()
myq.dequeue()
myq.dequeue()
myq.print_q()