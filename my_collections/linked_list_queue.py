from lists import Node


class LinkedListQueue:
    def __init__(self):  # type: (...) -> None
        self._head = self._tail = None

    def is_empty(self):  # type: () -> bool
        if self._head == self._tail is None:
            return True
        else:
            return False

    def enqueue(self, data):  # type: (...) -> Node
        if self.is_empty():
            new_node = Node(data)
            self._head = self._tail = new_node
            return self._tail
        else:
            new_node = Node(data)
            self._tail.next_node = new_node
            self._tail = new_node
            return self._tail

    def dequeue(self):  # type: () -> bool
        if self.is_empty():
            print("Queue is empty")
            return False
        else:
            if self._head == self._tail:
                self._head = self._tail = self._head.next_node
            else:
                self._head = self._head.next_node
            return True

    def peek(self):  # type: () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self._head.data)

    def print_queue(self):
        temp = self._head
        while temp is not None:
            print(temp.data)
            temp = temp.next_node

