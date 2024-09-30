import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# visited[0][0] = 1  # 시작점


def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 상하좌우: 행의 이동(2), 열의 이동(2)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # for i in range(N):
            #     print(maze[i])
            # 
            # print("-------------------")
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시
            if maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
        # (N, M)까지 최단거리 반환
    return maze[N - 1][M - 1]
#print(maze)
print(bfs(0, 0))
