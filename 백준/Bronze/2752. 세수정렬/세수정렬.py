import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
result = list(map(str, sorted(num)))

print(" ".join(result))
