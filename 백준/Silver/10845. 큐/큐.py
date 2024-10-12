import sys
input = sys.stdin.readline

class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def pushX(self, X):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = X

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            item = self.array[self.front]
            self.array[self.front] = None
            return item
        else:
            return -1

    def size(self):
        if not self.is_empty():
            return (self.rear - self.front + self.capacity) % self.capacity
        else:
            return 0

    def get_front(self):
        if not self.is_empty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            return -1

    def get_back(self):
        if not self.is_empty():
            return self.array[(self.rear)]
        else:
            return -1

N = int(input().strip())
q = ArrayQueue(N)

for i in range(N):
    order = input().strip()
    if "push" in order:
        order, n = order.split()
        q.pushX(n)
    elif order == "pop":
        print(q.pop())
    elif order == "size":
        print(q.size())
    elif order == "front":
        print(q.get_front())
    elif order == "back":
        print(q.get_back())
    elif order == "empty":
        print("1") if q.is_empty() else print("0")
    else:
        pass