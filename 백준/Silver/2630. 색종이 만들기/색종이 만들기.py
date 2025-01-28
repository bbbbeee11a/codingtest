def sol(arr, N):
    # 종료조건(base condition): 배열이 1 * 1 크기일 때
    if N == 1:
        return (1, 0) if arr[0][0] == 0 else (0, 1)

    # 배열이 모두 흰색일 경우
    if sum(map(sum, arr)) == 0:
        return (1, 0)

    # 배열이 모두 파란색일 경우
    if sum(map(sum, arr)) == N * N:
        return (0, 1)

    # 배열을 4등분하여 재귀 호출
    half = N // 2
    top_left = [row[:half] for row in arr[:half]]
    bottom_left = [row[:half] for row in arr[half:]]
    top_right = [row[half:] for row in arr[:half]]
    bottom_right = [row[half:] for row in arr[half:]]

    w1, b1 = sol(top_left, half)
    w2, b2 = sol(bottom_left, half)
    w3, b3 = sol(top_right, half)
    w4, b4 = sol(bottom_right, half)

    return (w1 + w2 + w3 + w4, b1 + b2 + b3 + b4)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
w, b = sol(arr, N)
print(w)
print(b)
