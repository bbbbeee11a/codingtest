while True:
    string = input().rstrip()

    if string == ".":
        break

    check = []
    is_balanced = True

    for ch in string:
        if ch == "(" or ch == "[":
            check.append(ch)
        elif ch == ")":
            if check and check[-1] == "(":
                check.pop()
            else:
                is_balanced = False
                break
        elif ch == "]":
            if check and check[-1] == "[":
                check.pop()
            else:
                is_balanced = False
                break

    if is_balanced and not check:
        print("yes")
    else:
        print("no")