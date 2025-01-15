import sys

input = sys.stdin.readline

word = input().rstrip()

cnt = 0
c_al = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for al in c_al:
    word = word.replace(al, "a")

print(len(word))