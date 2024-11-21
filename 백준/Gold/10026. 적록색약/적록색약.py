from collections import deque

n = int(input())
painting = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited_cb = [[False] * n for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y, visited):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or nx >= n or ny >= n or visited[nx][ny]:
                continue
            if painting[x][y] == painting[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, visited)
            cnt += 1
print(cnt, end=" ")

for i in range(n):
    for j in range(n):
        if painting[i][j] == "R":
            painting[i][j] = "G"

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited_cb[i][j]:
            bfs(i, j, visited_cb)
            cnt += 1
print(cnt)