from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_island(x, y, mark):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    maps[x][y] = mark

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                    maps[nx][ny] = mark
                    visited[nx][ny] = True


def bfs_path(island):
    q = deque()
    dist = [[-1] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maps[i][j] == island:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] != island and maps[nx][ny] != 0:  # 다른 섬과 만났을 경우
                    return dist[x][y]
                if maps[nx][ny] == 0 and dist[nx][ny] == -1:  # 물이고 아직 건너지 않은 곳일 경우
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


mark = 1  # 섬의 고유번호
for x in range(N):
    for y in range(N):
        if maps[x][y] == 1 and not visited[x][y]:
            island_cnt = bfs_island(x, y, mark)
            mark += 1

result = sys.maxsize  # 최댓값
for island in range(1, mark):
    result = min(result, bfs_path(island))
    
print(result)