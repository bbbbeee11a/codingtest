import sys
sys.setrecursionlimit(2500000)
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 방향 벡터(상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# dfs 함수 정의
def dfs(x, y):
	visited[x][y] = True  # 방문 표시
	size = 1  # 현재 그림의 크기
	
	# 상하좌우 탐색
	for dx, dy in directions:
		nx, ny = x + dx, y + dy
		if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
			size += dfs(nx, ny)
		
	return size


pic_cnt = 0  # 그림의 개수
max_size = 0  # 가장 큰 그림의 크기

for i in range(n):
	for j in range(m):
		if board[i][j] == 1 and not visited[i][j]:  # 그림이고 방문하지 않은 경우
				pic_cnt += 1
				max_size = max(max_size, dfs(i, j))

print(pic_cnt)
print(max_size)