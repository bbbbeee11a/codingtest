from collections import Counter

for _ in range(int(input())):
    a, b = input().split()
    print("Possible" if Counter(a) == Counter(b) else "Impossible")