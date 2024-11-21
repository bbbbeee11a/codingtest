import sys
input = sys.stdin.readline

def solution(A, N, M):
    left, right = 0, 0
    answer = float('inf')  
    while right < N:
        diff = A[right] - A[left]
        if diff == M:
            return M  
        elif diff > M:
            answer = min(answer, diff)
            left += 1
        else:
            right += 1
    return answer    

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]

A.sort()
print(solution(A, N, M))