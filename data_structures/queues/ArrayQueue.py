class ArrayQueue:
    def __init__(self, size=10):
        self._array = [None] * size
        self._front = self._rear = None
        self.size = size

    def isFull(self):
        if self._rear is self.size - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self._rear is None and self._front is None:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full")
        else:
            if self.isEmpty():
                self._front = self._rear = 0
                self._array[self._rear] = value
            else:
                self._rear += 1
                self._array[self._rear] = value

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            if self._rear is self._front:
                self._front = self._rear = -1
            else:
                self._front += 1

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self._array[self._front]



