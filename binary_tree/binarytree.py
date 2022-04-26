from nbformat import current_nbformat
from sympy import root


class Node():
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    def print_bt(self):
        pass

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left

    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def bfs(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(self.root)
        while len(queue) > 0 :
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result 

my_bt = BinaryTree()
my_bt.insert(6)
my_bt.insert(1)
my_bt.insert(4)
my_bt.insert(3)
my_bt.insert(7)
my_bt.insert(8)
my_bt.insert(9)

print(my_bt.bfs())