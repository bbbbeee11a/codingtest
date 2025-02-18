N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0] * 8

def func(k):
    if k == M:
        print(*ans[:M])
        return

    for i in range(N):
        if arr[i]:
            if ans[k - 1] < arr[i]:
                ans[k] = arr[i]
                temp = arr[i]
                arr[i] = 0
                func(k + 1)
                arr[i] = temp

func(0)
