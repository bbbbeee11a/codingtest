arr = [0] * 9
is_used = [0] * 9


def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if not is_used[i] and i > arr[k - 1]:
            arr[k] = i
            is_used[i] = 1
            func(k + 1)
            is_used[i] = 0

N, M = map(int, input().split())

func(0)
