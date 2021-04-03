class ArrayCyclicQueue:
    def __init__(self, capacity=10):  # type: (int) -> None
        self._array = [None] * capacity
        self._front = self._rear = -1
        self.capacity = capacity

    def is_full(self):  # type: () -> bool
        if (self._rear + 1) % self.capacity == self._front:
            print("Queue is full")
            return True
        else:
            return False

    def is_empty(self):  # type: () -> bool
        if self._rear is -1 and self._front is -1:
            print("Queue is empty")
            return True
        else:
            return False

    def enqueue(self, data):  # type (...) -> bool
        if self.is_full():
            return False
        else:
            if self.is_empty():
                self._front = self._rear = 0
                self._array[self._rear] = data
                return True
            else:
                self._rear = (self._rear + 1) % self.capacity
                self._array[self._rear] = data
                return True

    def dequeue(self):  # type () -> bool
        if self.is_empty():
            return False
        else:
            if self._front is self._rear:
                self._rear = self._front = -1
                return True
            else:
                self._front = (self._front + 1) % self.capacity
                return True

    def peek(self):  # type () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self._array[self._front])

    def print_queue(self):  # type () -> None
        if self.is_empty():
            print("Queue is empty")
        else:
            pointer = self._front
            while pointer is not self._rear:
                print(self._array[pointer])
                pointer = (pointer + 1) % self.capacity
            print(self._array[self._rear])



