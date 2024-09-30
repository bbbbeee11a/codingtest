from collections import deque, defaultdict
from itertools import combinations

def bfs(graph, begin, target, visited):
    queue = deque([begin])
    visited[begin] = 1
    cnt = 0

    while queue:
        # 현재 레벨에서 탐색할 노드 수
        level_size = len(queue)
        cnt += 1  # 레벨이 증가할 때마다 거리 증가

        for _ in range(level_size):
            x = queue.popleft()

            for i in graph[x]:
                if visited[i] == 0:
                    if i == target:
                        return cnt
                    queue.append(i)
                    visited[i] = 1

    # target을 찾지 못할 경우 0을 반환
    return 0


def solution(begin, target, words):
    graph = defaultdict(list)
    visited = defaultdict(list)

    words.append(begin)
    for word in words:
        visited[word] = 0

    combi = list(combinations(words, 2))
    for a, b in combi:
        count = 0
        for i in range(len(begin)):
            if a[i] == b[i]:
                count += 1
        if count == len(begin) - 1:
            graph[a].append(b)
            graph[b].append(a)

    if target not in words:
        return 0

    return bfs(graph, begin, target, visited)