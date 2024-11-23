import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
target = int(input())

left, right = 0, n - 1
cnt = 0

while left < right:
    s = arr[left] + arr[right]
    if s == target:
        cnt += 1
        left += 1
        right -= 1
    elif s > target:
        right -= 1
    else:  # s < target
        left += 1

print(cnt)