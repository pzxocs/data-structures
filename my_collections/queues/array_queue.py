class ArrayQueue:
    def __init__(self, capacity=10):  # type: (int) -> None
        self._array = [None] * capacity
        self._front = self._rear = -1
        self.capacity = capacity

    def is_full(self):  # type: () -> bool
        if self._rear is self.capacity - 1:
            return True
        else:
            return False

    def is_empty(self):  # type: () -> bool
        if self._rear is -1 and  self._front is -1:
            return True
        else:
            return False

    def enqueue(self, value):  # type: (...) -> bool
        if self.is_full():
            print("Queue is full")
            return False
        else:
            if self.is_empty():
                self._front = self._rear = 0
            else:
                self._rear += 1
            self._array[self._rear] = value
            return True

    def dequeue(self):  # type: (...)-> bool
        if self.is_empty():
            print("Queue is empty")
            return False
        else:
            if self._rear is self._front:
                self._front = self._rear = -1
            else:
                self._front += 1
            return True

    def peek(self):  # type: () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            print (self._array[self._front])

    def print_queue(self):  # type: () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            pointer = self._front
            print(self._array[pointer])
            while pointer is not self._rear:
                pointer += 1
                print(self._array[pointer])





