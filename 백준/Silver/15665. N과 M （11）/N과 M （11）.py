N, M = map(int, input().split())
arr = (sorted(list(set(map(int, input().split())))))
arr_len = len(arr)
visited = [0] * N
ans = []
prev = []

def sol(k):
    global prev

    if k == M:
        if ans != prev:
            print(*ans)
            prev = ans.copy()
        return

    for i in range(arr_len):
        ans.append(arr[i])
        sol(k + 1)
        ans.pop()


sol(0)