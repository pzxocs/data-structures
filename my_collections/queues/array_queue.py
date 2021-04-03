class ArrayQueue:

    def __init__(self, size=10):  # type: (int) -> None
        self._array = [None] * size
        self._front = self._rear = None
        self.size = size

    def is_full(self):  # type: () -> bool
        if self._rear is self.size - 1:
            return True
        else:
            return False

    def is_empty(self):  # type: () -> bool
        if self._rear is None and self._front is None:
            return True
        else:
            return False

    def enqueue(self, value):  # type: (...)-> bool
        if self.is_full():
            print("Queue is full")
            return False
        else:
            if self.is_empty():
                self._front = self._rear = 0
                self._array[self._rear] = value
                return True
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
                return True
            else:
                self._front += 1
                return True

    def peek(self):  # type: ()-> ...
        if self.is_empty():
            print("Queue is empty")
            return False
        else:
            return self._array[self._front]



