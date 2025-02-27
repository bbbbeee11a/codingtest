visited = []
ans = []
def sol(n):
    if n == 6:
        print(*ans)
        return

    for i in range(k):
        if (len(ans) == 0 or arr[i] > ans[-1]) and not visited[i]:
            ans.append(arr[i])
            visited[i] = 1
            sol(n + 1)
            visited[i] = 0
            ans.pop()


while True:
    arr = list()
    arr = list(map(int, input().split()))
    k, arr = arr[0], arr[1:]
    if k == 0:
        break
    visited = [0] * k
    sol(0)
    print()
