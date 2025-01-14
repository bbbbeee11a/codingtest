import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
answer = 0

for cards in combinations(num, 3):
    total = sum(cards)

    if total <= m:
        answer = max(answer, total)
        if total == m:
            break

print(answer)