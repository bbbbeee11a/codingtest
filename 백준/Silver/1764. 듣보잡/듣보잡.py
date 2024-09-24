import sys

N, M = map(int, input().split())
A = set()
B = set()

for _ in range(N):
    A.add(sys.stdin.readline().strip())
for _ in range(M):
    B.add(sys.stdin.readline().strip())

answer = sorted(A.intersection(B))

print(len(answer))
for name in answer:
    print(name)