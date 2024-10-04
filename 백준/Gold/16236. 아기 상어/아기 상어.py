from collections import deque

INF = 1e9  # 무한을 의미하는 값으로 10억을 설정

n = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 아기 상어의 현재 크기와 위치
cur_size = 2
cur_x, cur_y = 0, 0

# 아기 상어의 시작 위치를 찾은 뒤에 그 위치에는 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            cur_x, cur_y = i, j
            arr[cur_x][cur_y] = 0


# 모든 위치까지 '최단 거리'만 계산
def bfs():
    # -1이면 도달 불가
    dist = [[-1] * n for _ in range(n)]

    # 시작 위치는 도달 가능, 거리 0
    q = deque([(cur_x, cur_y)])  # 수정: 튜플 형식으로 큐에 추가
    dist[cur_x][cur_y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:  # 수정: ny > n -> ny >= n
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and arr[nx][ny] <= cur_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    # 모든 위치까지의 최단 거리 테이블 반환
    return dist


# 최단 거리 테이블을 활용해 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF

    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and arr[i][j] >= 1 and arr[i][j] < cur_size:  # 수정: arr[i][j] < cur_size
                # 가장 가까운 한 마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:  # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x, y, min_dist


result = 0
ate = 0

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우 현재까지 움직인 거리 출력
    if value is None:
        print(result)
        break

    else:
        # 현재 위치 갱신 및 이동 거리 변경
        cur_x, cur_y = value[0], value[1]
        result += value[2]
        # 먹은 위치는 0으로 초기화
        arr[cur_x][cur_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= cur_size:
            cur_size += 1
            ate = 0