import sys
from collections import deque

input = sys.stdin.readline
d = deque()

for _ in range(int(input())):
    order = input().split()

    if order[0] == "push_front":
        d.appendleft(order[1])
    elif order[0] == "push_back":
        d.append(order[1])
    elif order[0] == "pop_front":
        print(d.popleft() if d else -1)
    elif order[0] == "pop_back":
        print(d.pop() if d else -1)
    elif order[0] == "size":
        print(len(d))
    elif order[0] == "empty":
        print(0 if d else 1)
    elif order[0] == "front":
        print(d[0] if d else -1)
    elif order[0] == "back":
        print(d[-1] if d else -1)