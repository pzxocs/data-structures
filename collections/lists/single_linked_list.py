from node import *


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        temp = self.head
        while temp.next_node is not None:
            temp = temp.next_node
        temp.next_node = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node
