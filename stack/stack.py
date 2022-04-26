class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        temp = self.top
        if self.height == 0 :
            return None
        else:
            self.top = temp.next
            temp.next = None
            self.height -= 1
        return temp


my_stack = Stack(3)
my_stack.push(4)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print_stack()