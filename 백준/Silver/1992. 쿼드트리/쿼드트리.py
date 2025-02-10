import sys
input = sys.stdin.readline

def sol(arr, N):
    # base condition
    if N == 1:
        result.append("1" if arr[0][0] == 1 else "0")
        return

    # 배열 전체가 0인 경우
    if sum(map(sum, arr)) == 0:
        result.append("0")
        return

    # 배열 전체가 1인 경우
    if sum(map(sum, arr)) == N * N:
        result.append("1")
        return

    # 압축 불가능한 경우, 4등분으로 나누어 재귀 호출
    half = N // 2
    top_left = [row[:half] for row in arr[:half]]
    top_right = [row[half:] for row in arr[:half]]
    bottom_left = [row[:half] for row in arr[half:]]
    bottom_right = [row[half:] for row in arr[half:]]

    result.append("(")
    sol(top_left, half)
    sol(top_right, half)
    sol(bottom_left, half)
    sol(bottom_right, half)
    result.append(")")

N = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(N)]
result = []
sol(arr, N)
print("".join(result))
