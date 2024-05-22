import sys

def cal(a, b, c: int):
    # 평균 * 3: a + b + c
    # 중앙값 * 3: 3 * b
    # a, b, c는 크기순으로 정렬되어 있다고 가정
    return abs(a + b + c - 3 * b)


N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

A.sort()

answer = -1
for i in range(1, N-1):
    # 중앙값: A[i]
    answer = max(answer, cal(A[i - 1], A[i], A[N - 1]))  # 평균이 최대인 경우
    answer = max(answer, cal(A[0], A[i], A[i + 1])) # 평균이 최소인 경우

print(answer)