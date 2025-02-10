import sys
input = sys.stdin.readline


def is_all_zero(matrix):
    return not any(cell != 0 for row in matrix for cell in row)


def sol(arr, N):
    # base condition(종료조건)
    if N == 1:
        if arr[0][0] == -1:
            return (1, 0, 0)
        elif arr[0][0] == 0:
            return (0, 1, 0)
        else:
            return (0, 0, 1)

    # 종이가 모두 같은 수인 경우
    total = sum(map(sum, arr))

    if is_all_zero(arr):
        return (0, 1, 0)
    if total == -(N * N):
        return (1, 0, 0)
    if total == N * N:
        return (0, 0, 1)

    # 종이가 서로 다른 수로 이루어져있는 경우
    unit = N // 3

    unit_1 = [row[:unit] for row in arr[:unit]]
    unit_2 = [row[unit:unit * 2] for row in arr[:unit]]
    unit_3 = [row[unit * 2:] for row in arr[:unit]]
    unit_4 = [row[:unit] for row in arr[unit:2 * unit]]
    unit_5 = [row[unit:unit * 2] for row in arr[unit:2 * unit]]
    unit_6 = [row[unit * 2:] for row in arr[unit:2 * unit]]
    unit_7 = [row[:unit] for row in arr[2 * unit:]]
    unit_8 = [row[unit:unit * 2] for row in arr[2 * unit:]]
    unit_9 = [row[unit * 2:] for row in arr[2 * unit:]]

    x1, y1, z1 = sol(unit_1, unit)
    x2, y2, z2 = sol(unit_2, unit)
    x3, y3, z3 = sol(unit_3, unit)
    x4, y4, z4 = sol(unit_4, unit)
    x5, y5, z5 = sol(unit_5, unit)
    x6, y6, z6 = sol(unit_6, unit)
    x7, y7, z7 = sol(unit_7, unit)
    x8, y8, z8 = sol(unit_8, unit)
    x9, y9, z9 = sol(unit_9, unit)

    return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9, y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9,
        z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
x, y, z = sol(arr, N)
print(x)
print(y)
print(z)
