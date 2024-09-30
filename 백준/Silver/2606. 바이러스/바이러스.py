n = int(input())
v = int(input())

graph = [[] for i in range(n + 1)]  # 그래프 초기화
visited = [0] * (n + 1)  # 방문한 컴퓨터인지 표시

for i in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]  # 양방향 그래프 연결


def dfs(v):
    visited[v] = 1
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited) - 1)
