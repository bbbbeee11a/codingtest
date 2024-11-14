# 푸는 데 걸린 시간:
import math

n = list(str(input()))

arr = [0] * 10

for num in n:
    arr[int(num)] += 1

result = 0

if arr[6] + arr[9] >= 2:
    arr[6] = math.ceil((arr[6] + arr[9]) / 2.0)
    arr[9] = 0

print(max(arr))