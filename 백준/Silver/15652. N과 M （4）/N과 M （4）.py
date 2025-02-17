arr = [0] * 9

def func(k):
    if k > M:
        for i in range(1, M + 1):
            print(arr[i], end=' ')
        print()
        return

    for i in range(arr[k - 1], N + 1):
        arr[k] = i
        func(k + 1)

N, M = map(int, input().split())

arr[0] = 1
func(1)