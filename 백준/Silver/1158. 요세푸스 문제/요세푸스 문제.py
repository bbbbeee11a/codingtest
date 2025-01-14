from collections import deque

n, k = map(int, input().split())
answer = list()
d = deque(i for i in range(1, n + 1))

while d:
    d.rotate(-(k - 1))
    answer.append(d.popleft())

print("<", end='')
for i in range(len(answer) - 1):
    print(answer[i], end=", ")
print(f"{answer[-1]}", end="")
print(">")