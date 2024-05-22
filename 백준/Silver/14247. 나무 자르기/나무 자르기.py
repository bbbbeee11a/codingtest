import sys

n = int(sys.stdin.readline())
H = list(map(int, input().split()))
A = list(map(int, input().split()))

A.sort()

total = 0
for i in range(n):
    total += A[i] * i + H[i]

print(total)
