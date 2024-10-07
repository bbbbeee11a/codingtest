def is_vps(ps):
    li = []
    for i in ps:
        if i == '(':
            li.append(i)
        else:
            if li:  # list is not empty
                if li.pop() != '(':
                    return False
            else:  # list is empty
                return False
        # print(li)
    return True if not li else False

n = int(input())

for _ in range(n):
    ps = input()
    print("YES") if is_vps(ps) else print("NO")