N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
w, b = 0, 0

def div_conq(x, y, N):
    global w, b
    tmp = 0

    for i in range(x, x + N):
        for j in range(y, y + N):
            if arr[i][j]:
                tmp += 1

    if not tmp:
        w += 1

    elif tmp == N ** 2:
        b += 1

    else:
        div_conq(x, y, N // 2)
        div_conq(x + N // 2, y, N // 2)
        div_conq(x, y + N // 2, N // 2)
        div_conq(x + N // 2, y + N // 2, N // 2)

div_conq(0, 0, N)
print(w)
print(b)
