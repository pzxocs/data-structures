from lists import Node


class LinkedListQueue:
    def __init__(self):  # type: () -> None
        self._front = self._rear = None

    def is_empty(self):  # type: () -> bool
        if self._front == self._rear is None:
            return True
        else:
            return False

    def enqueue(self, data):  # type: (...) -> Node
        new_node = Node(data)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next_node = new_node
            self._rear = new_node
        return self._rear

    def dequeue(self):  # type: () -> bool
        if self.is_empty():
            print("Queue is empty")
            return False
        else:
            if self._front == self._rear:
                self._front = self._rear = self._front.next_node
            else:
                self._front = self._front.next_node
            return True

    def peek(self):  # type: () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self._front.data)

    def print_queue(self):
        temp = self._front
        while temp is not None:
            print(temp.data)
            temp = temp.next_node

