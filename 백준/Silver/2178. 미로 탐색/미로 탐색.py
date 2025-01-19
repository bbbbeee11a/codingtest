from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(x, y):
    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()

        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = arr[cx][cy] + 1
                q.append((nx, ny))

    return arr[n - 1][m - 1]

print(bfs(0, 0))