from collections import deque

n = int(input())

arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))


    return cnt


total = 0
result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            total += 1
            result.append(bfs(i, j))

print(total)
print("\n".join(map(str, sorted(result))))
