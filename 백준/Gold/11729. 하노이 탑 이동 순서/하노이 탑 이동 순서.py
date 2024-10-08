# 하노이 탑 문제의 최소 이동 횟수: 2 ** n - 1
def hanoi_tower(n, frm, tmp, to):
    if n == 1:
        print(frm, to)
    else:
        hanoi_tower(n - 1, frm, to, tmp)
        print(frm, to)
        hanoi_tower(n - 1, tmp, frm, to)

N = int(input())
print(2 ** N - 1)
hanoi_tower(N, "1", "2", "3")
