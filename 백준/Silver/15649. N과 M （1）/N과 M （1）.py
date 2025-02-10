import itertools

N, M = map(int, input().split())

nPr = itertools.permutations([i for i in range(1, N + 1)], M)

for item in list(nPr):
    print(*item)
