import itertools

N, M = map(int, input().split())
nCr = itertools.combinations(list(i for i in range(1, N + 1)), M)
for item in nCr:
    print(*item)
    