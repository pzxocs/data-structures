from lists import Node


class LinkedListCyclicQueue:
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
        self._rear.next_node = self._front
        return new_node

    def dequeue(self):  # type: () -> bool
        if self.is_empty():
            print("Queue is empty")
            return False
        elif self._front is self._rear:
            self._front = self._rear = None
        else:
            self._front = self._front.next_node
            self._rear.next_node = self._front
        return True

    def peek(self):  # type: () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self._front.data)

    def print_queue(self):  # type: () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            temp = self._front
            while temp.next_node is not self._front:
                print(temp.data)
                temp = temp.next_node
            print(temp.data)


