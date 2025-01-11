import sys

input = sys.stdin.readline

result = 0

for _ in range(int(input())):
    word = list(input().rstrip())
    check = list()

    for w in word:
        if check:
            pair = check[-1]
        else:
            pair = ''

        if w == pair:
            check.pop()
            continue
        else:
            check.append(w)

    if not check:
        result += 1

print(result)
