N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0


def func(cur, total):
    global cnt

    if cur == N:
        if total == S: cnt += 1
        return

    func(cur + 1, total)
    func(cur + 1, total + arr[cur])

func(0, 0)

if S == 0: cnt -=1

print(cnt)
