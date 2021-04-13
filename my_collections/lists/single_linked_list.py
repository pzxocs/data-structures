from node import *


class SingleLinkedList:
    def __init__(self, data=None, next_node=None):  # type: (...) -> None
        self._front = Node(data, next_node)

    def is_empty(self):
        # type: () -> bool
        return self._head.data is None

    def prepend(self, data):  # type: (...) -> Node
        buff_node = Node(self._front.data, self._front.next_node)
        self._front.data = data
        self._front.next_node = buff_node
        self._front = Node(data, buff_node)
        return self._front

    def append(self, data):  # type: (...) -> Node
        new_node = Node(data)
        if self.is_empty():
            self._front = new_node
            return new_node
        temp = self._front

        while temp.next_node is not None:
            temp = temp.next_node

        temp.next_node = new_node
        return new_node

    def remove_first(self):  # type: () -> bool
        if self.is_empty():
            return False
        else:
            self._head = self._head.next_node
            return True

    def remove_last(self):  # type: () -> bool
        if self.is_empty():
            return False
        else:
            temp_target = self._head
            temp_before_target = None

            while temp_target.next_node is not None:
                temp_before_target = temp_target
                temp_target = temp_target.next_node

            temp_before_target.next_node = None
            return True

    def remove_by_value(self, value):  # type: (...) -> bool
        if self.is_empty():
            return False
        else:
            temp_before_target = Node(None, None)
            temp_target = self._front

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
                return False

    def insert_after_value(self, node_value, insert_value):  # type: (...) -> bool
        if self.is_empty():
            return False

        target_node = self._front

        while (target_node.data is not node_value and
               target_node.next_node is not None):
            target_node = target_node.next_node

        if target_node.data is node_value:
            new_node = Node(insert_value, next_node=target_node.next_node)
            target_node.next_node = new_node
            return True
        else:
            return False

    def print_list(self):
        temp = self._head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node
