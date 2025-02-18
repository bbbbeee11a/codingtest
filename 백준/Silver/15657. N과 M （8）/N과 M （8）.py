N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = [0] * 9

def func(k):
    if k == M:
        print(*ans[:M])
        return

    for i in range(N):
        if arr[i] and ans[k - 1] <= arr[i]:
            ans[k] = arr[i]
            func(k + 1)


func(0)
