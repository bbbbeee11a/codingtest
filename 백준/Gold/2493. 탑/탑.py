import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and stack[-1][1] < tower[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1][0] + 1

    stack.append((i, tower[i]))

print(" ".join(map(str, answer)))
