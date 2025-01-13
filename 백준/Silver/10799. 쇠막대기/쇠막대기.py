p = list(input().rstrip())

pipe = 0
check = list()
prev = ''

for i in p:
    if i == '(':
        check.append(i)
    elif i == ')':

        if prev == '(':  # () 레이저
            check.pop()
            pipe += len(check)
        elif prev == ')':
            check.pop()
            pipe += 1

    else:
        exit(0)

    prev = i


print(pipe)
