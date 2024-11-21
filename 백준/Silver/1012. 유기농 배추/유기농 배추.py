
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(board, x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(board, i, j)
                cnt += 1
    print(cnt)