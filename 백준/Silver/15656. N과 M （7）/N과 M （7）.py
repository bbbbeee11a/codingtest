N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0] * 8

def func(k):
    if k == M:
        print(*ans[:M])
        return

    for i in range(N):
        if arr[i]:
            ans[k] = arr[i]
            func(k + 1)

func(0)
