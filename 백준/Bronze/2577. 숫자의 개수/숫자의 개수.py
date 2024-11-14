n = 1
for _ in range(3):
    n *= int(input())

arr = [0] * 10
for num in str(n):
    arr[int(num)] += 1

any(print(num) for num in arr)