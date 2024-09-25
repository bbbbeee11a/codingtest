import itertools
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(" ")))

nPr = itertools.permutations(A, N)
sum = 0
max_sum = 0
for li in nPr:
    sum = 0
    for i in range(2, len(li) + 1):
        sum += abs(li[i - 2] - li[i - 1])
    max_sum = max(max_sum, sum)
    
print(max_sum)
