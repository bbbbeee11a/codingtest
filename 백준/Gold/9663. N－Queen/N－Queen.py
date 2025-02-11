is_used_1 = [0] * 15  # 열 방향 일치를 확인
is_used_2 = [0] * 30  # 우상향 대각선 일치를 확인
is_used_3 = [0] * 30  # 우하향 대각선 일치를 확인
cnt = 0

def func(cur):
    global cnt
    if cur == n:
        cnt += 1
        return

    for i in range(n):
        if is_used_1[i] or is_used_2[cur + i] or is_used_3[cur - i + n - 1]:
            continue
        # (cur, i)에 퀸을 둘 수 있다면 used 처리
        is_used_1[i] = 1
        is_used_2[cur + i] = 1
        is_used_3[cur - i + n - 1] = 1
        func(cur + 1)
        is_used_1[i] = 0
        is_used_2[cur + i] = 0
        is_used_3[cur - i + n - 1] = 0


n = int(input())

func(0)
print(cnt)
