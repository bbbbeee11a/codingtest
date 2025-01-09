from collections import deque

n, m = map(int, input().split())
targets = [int(i) for i in input().split()]
queue = deque([i for i in range(1, n + 1)])

result = 0
for target in targets:
    mid = len(queue) // 2
    x = 0
    
    loc = queue.index(target)
    if queue.index(target) <= mid:
        cnt = loc
        queue.rotate(-cnt)

    else:
        cnt = len(queue) - loc
        queue.rotate(cnt)

    result += cnt
    queue.popleft()

print(result)