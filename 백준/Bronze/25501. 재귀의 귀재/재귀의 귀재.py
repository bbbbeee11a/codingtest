def recursion(s: str, l: int, r: int, cnt: int):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        cnt += 1
        return recursion(s, l + 1, r - 1, cnt)


def is_palindrome(s: str) -> int:
    cnt = 1
    return recursion(s, 0, len(s) - 1, cnt)


for _ in range(int(input())):
    case = input().strip()
    print(*is_palindrome(case))
    