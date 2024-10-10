import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

left = 0
right = n - 1
cnt = 0

nums.sort()

while left < right:
    current_sum = nums[left] + nums[right]

    if current_sum == x:
        left += 1
        right -= 1
        cnt += 1
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print(cnt)
