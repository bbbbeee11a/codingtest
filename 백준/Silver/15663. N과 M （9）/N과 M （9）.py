N, M = map(int, input().split())
arr = (sorted(list(map(int, input().split()))))
visited = [0] * N
ans = []

def sol(k):
    check = 0
    
    if k == M:
        print(*ans)
        return
    
    for i in range(N):
        if check != arr[i] and not visited[i]:
            ans.append(arr[i])
            visited[i] = 1
            check = arr[i]
            sol(k + 1)
            ans.pop()
            visited[i] = 0

sol(0)
