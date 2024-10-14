from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
nge = list(map(int, input().split()))

answer = [-1] * N
stack = deque([(nge[0], 0)])  # value, index 순

for i in range(1, N):
    while stack and stack[-1][0] < nge[i]:
        val, idx = stack.pop()
        answer[idx] = nge[i]

    stack.append((nge[i], i))

print(*answer)