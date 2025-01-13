stack = list()
string = input().rstrip()
temp = 1
result = 0

for i, p in enumerate(string):
    if p == '(':
        temp *= 2
        stack.append(p)
    elif p == '[':
        temp *= 3
        stack.append(p)
    elif p == ')':
        if not stack or stack[-1] != '(':
            print(0)
            exit()
        if string[i - 1] == '(':
            result += temp
        stack.pop()
        temp //= 2
    elif p == ']':
        if not stack or stack[-1] != '[':
            print(0)
            exit()
        if string[i - 1] == '[':
            result += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(result)
    