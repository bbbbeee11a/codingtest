from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

def bfs():
	queue = deque()
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	
	for i in range(n):
		for j in range(m):
			if box[i][j] == 1:
				queue.append((i, j))
	
	while queue:
		x, y = queue.popleft()
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
				box[nx][ny] = box[x][y] + 1
				queue.append((nx, ny))
				
bfs()

result = 0
for row in box:
	if 0 in row:
		print(-1)
		exit()
	result = max(result, max(row))
	
print(result - 1)		
