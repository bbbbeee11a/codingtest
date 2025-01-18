N, r, c = map(int, input().split())

def sol2(N, r, c):
    if N == 0:
        return 0

    half = 2 ** (N - 1)
    if r < half and c < half:  # 1번 사각형(제2사분면)
        return sol2(N - 1, r, c)
    elif r < half and c >= half:  # 2번 사각형(제1사분면)
        return half * half + sol2(N - 1, r, c - half)
    elif r >= half and c < half:  # 3번 사각형(제3사분면)
        return 2 * half * half + sol2(N - 1, r - half, c)

    return 3 * half * half + sol2(N - 1, r - half, c - half)  # 4번 사격형(제4사분면)

print(sol2(N, r, c))