import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))

max_sum = 0
visited = [False] * N

def backtrack(current_permutation, current_sum):
    global max_sum
    
    if len(current_permutation) == N:
        max_sum = max(max_sum, current_sum)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            if len(current_permutation) > 0:
                next_sum = current_sum + abs(A[i] - A[current_permutation[-1]])
            else:
                next_sum = current_sum
            backtrack(current_permutation + [i], next_sum)
            visited[i] = False

backtrack([], 0)
print(max_sum)