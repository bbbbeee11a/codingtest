import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):  # t만큼 반복
    is_reverse = False
    err = False
    p = input().rstrip()
    n = int(input())

    # 빈 배열 처리
    arr = input().rstrip().strip("[]")
    arr = deque(arr.split(",")) if arr else deque()

    for ac in p:
        if ac == "R":
            is_reverse = not is_reverse
        elif ac == "D":
            if not arr:
                err = True
                break
            if is_reverse:
                arr.pop()
            else:
                arr.popleft()

    if err:
        print("error")
    else:
        if is_reverse:
            arr = list(reversed(arr))
        print(f"[{','.join(arr)}]")