def rec(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = rec(a, b // 2, c)
        return (half * half) % c
    else:
        return (a * rec(a, b - 1, c)) % c

a, b, c = map(int, input().split())
print(rec(a, b, c))