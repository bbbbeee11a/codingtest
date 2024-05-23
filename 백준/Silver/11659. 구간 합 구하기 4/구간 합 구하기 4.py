import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
psum = [0] * N
psum[0] = A[0]
for i in range(1, N):
    psum[i] = psum[i - 1] + A[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(psum[j - 1] - psum[i - 2] if i > 1 else psum[j - 1])
