import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

# 노드를 오름차순으로 방문하기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for nx in graph[v]:
        if visited[nx] == 0:
            dfs(nx)


def bfs(v):
    q = deque([v])
    visited[v] = 1
    print()
    print(v, end=" ")
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                print(i, end=" ")


dfs(V)
visited = [0] * (N + 1)
bfs(V)
