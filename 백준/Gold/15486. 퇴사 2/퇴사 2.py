import sys

input = sys.stdin.readline

N = int(input())

# zip의 결과를 리스트로 변환하고, 인덱스 1부터 시작하기 위해 0을 앞에 추가
t, p = map(list, zip(*([(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)])))

# N일차까지 얻을 수 있는 최대 이익
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])  # i일차까지의 최댓값
    fin_date = i + t[i] - 1  # i일차에 행하는 일의 종료일
    if fin_date <= N:
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])

print(max(dp))
