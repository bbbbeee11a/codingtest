from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

# 방향 설정: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, r, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maps[nx][ny] > r:
                visited[nx][ny] = True
                queue.append((nx, ny))

def find_safe_zones(r):
    visited = [[False] * N for _ in range(N)]
    safe_zone_count = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] > r and not visited[i][j]:
                bfs(i, j, r, visited)
                safe_zone_count += 1

    return safe_zone_count

max_safe_zones = 0
max_height = max(map(max, maps))

for r in range(max_height + 1):
    max_safe_zones = max(max_safe_zones, find_safe_zones(r))

print(max_safe_zones)