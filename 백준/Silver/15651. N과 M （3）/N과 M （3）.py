arr = [0] * 7
is_used = [0] * 8


def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        arr[k] = i
        func(k + 1)

N, M = map(int, input().split())

func(0)
