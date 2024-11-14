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

while any(num > 0 for num in arr):
    if all(num <= 1 for num in arr):
        result += 1
        break
        
    for i in range(9):
        if arr[i] > 0:
            arr[i] -= 1
    result += 1


print(result)