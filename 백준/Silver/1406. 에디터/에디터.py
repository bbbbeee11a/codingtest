from collections import deque
import sys

input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()

for _ in range(int(input())):
    command = input().split()
    if command[0] == "P":
        left.append(command[1])
    elif command[0] == "B":
        if left:
            left.pop()
    elif command[0] == "L":
        if left:
            right.appendleft(left.pop())
    elif command[0] == "D":
        if right:
            left.append(right.popleft())

print("".join(left + right))
