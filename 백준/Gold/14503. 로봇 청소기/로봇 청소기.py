N, M = map(int, input().split())
# d가 0: 북, 1: 동, 2: 남, 3: 서
r, c, d = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 순서
dx = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dy = [0, 1, 0, -1]  # 상, 우, 하, 좌


def get_direction(d):
    # 반시계 방향으로 회전 (d: 0 -> 3, 1 -> 0, 2 -> 1, 3 -> 2)
    return (d - 1) % 4


def back_direction(d):
    # 후진하는 방향은 현재 방향에서 180도 회전한 방향
    return (d + 2) % 4


def sol(x, y, d):
    # 현재 위치를 청소
    answer = 0
    if maps[x][y] == 0:  # 현재 칸이 청소되지 않았으면 청소
        maps[x][y] = 2  # 청소 완료 표시(0: 청소 안 함, 1: 벽)
        answer += 1

    # 현재 칸 주변 4칸 탐색
    for _ in range(4):
        d = get_direction(d)  # 반시계 방향으로 회전
        nx = x + dx[d]
        ny = y + dy[d]

        # 지도 범위를 벗어나지 않고, 청소되지 않은 빈칸이 있으면 그쪽으로 이동
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
            answer += sol(nx, ny, d)  # 새로운 위치로 이동 후 재귀 탐색
            return answer  # 이동한 경우는 바로 탐색을 종료하고 돌아감

    # 네 방향 모두 청소되어 있거나 벽인 경우 후진 시도
    back_d = back_direction(d)
    nx = x + dx[back_d]
    ny = y + dy[back_d]

    if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] != 1:  # 후진 가능하면 후진
        answer += sol(nx, ny, d)  # 방향은 유지한 채 후진

    return answer


# 탐색 시작
print(sol(r, c, d))
