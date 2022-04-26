import enum
from sympy import Order


class HashTable():
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23 ) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, v in enumerate(self.data_map):
            print(i, " : ", v)

    def set_item(self,key,value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
        return True

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for k, v in self.data_map[index]:
                if k == key:
                    return v
        return None 

    def keys(self):
        key_list = []
        for section in self.data_map:
            if section is not None:
                for k,v in section:
                    key_list.append(k)
        return key_list

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 20)
my_hash_table.set_item("lumber", 210)

print(my_hash_table.keys())