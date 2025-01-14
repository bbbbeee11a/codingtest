import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    pw = list(input().rstrip())
    left = deque()
    right = deque()

    for i in range(len(pw)):
        x = pw[i]

        if x == "<":
            if left:
                right.appendleft(left.pop())

        elif x == ">":
            if right:
                left.append(right.popleft())
        elif x == "-":
            if left:
                left.pop()
        else:
            left.append(x)

    print("".join(left + right))
