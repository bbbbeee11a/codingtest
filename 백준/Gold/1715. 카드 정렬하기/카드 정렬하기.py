import heapq
import sys
input = sys.stdin.readline

N = int(input())
cards = []

for _ in range(N):
    heapq.heappush(cards, int(input()))

total = 0
while len(cards) > 1:
    # 가장 작은 두 묶음을 더한다
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    result = a + b
    total += result
    heapq.heappush(cards, result)

print(total)