from node import *


class SingleLinkedList:
    def __init__(self, data=None, next_node=None):
        # type: (...) -> None
        self.head = Node(data, next_node)

    def is_empty(self):
        # type: () -> bool
        return self.head.data is None

    def prepend(self, data):
        # type: (...) -> None
        buff_node = Node(self.head.data, self.head.next_node)
        self.head.data = data
        self.head.next_node = buff_node
        self.head = Node(data, buff_node)

    def append(self, data):
        # type: (...) -> None
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        temp = self.head

        while temp.next_node is not None:
            temp = temp.next_node

        temp.next_node = new_node

    def remove_first(self):
        # type: () -> bool
        if self.is_empty():
            print ("List is empty")
            return False
        else:
            self.head = self.head.next_node
            return True

    def remove_last(self):
        # type: () -> bool
        if self.is_empty():
            print ("List is empty")
            return False
        else:
            temp_target = self.head
            temp_before_target = None

            while temp_target.next_node is not None:
                temp_before_target = temp_target
                temp_target = temp_target.next_node

            temp_before_target.next_node = None
            return True

    def remove_by_value(self, value):
        # type: (...) -> bool
        if self.is_empty():
            print ("List is empty")
            return False
        else:
            temp_before_target = Node(None, None)
            temp_target = self.head

            if temp_target.data is value:
                self.remove_first()
                return True

            while (temp_target.data is not value and
                   temp_target.next_node is not None):
                temp_before_target = temp_target
                temp_target = temp_target.next_node

            if temp_target.data is value:
                temp_before_target.next_node = temp_target.next_node
            else:
                print("No such value in the list")
                return False

    def insert_after_value(self, node_value, insert_value):
        # type: (...) -> bool
        if self.is_empty():
            print("List is empty")
            return False

        target_node = self.head

        while (target_node.data is not node_value and
               target_node.next_node is not None):
            target_node = target_node.next_node

        if target_node.data is node_value:
            new_node = Node(insert_value, next_node=target_node.next_node)
            target_node.next_node = new_node
            return True
        else:
            print("No such value in the list")
            return False

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node