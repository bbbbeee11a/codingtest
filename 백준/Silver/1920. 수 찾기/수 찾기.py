import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr = sorted(a)

def bin_search(x):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if x == arr[mid]:
            break
        elif x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
            
    return arr[mid]


for target in targets:
    print(1) if target == bin_search(target) else print(0)