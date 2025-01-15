li = []
for _ in range(5):
    li.append(list(input().rstrip()))

answer = ''

length = 0
for r in li:
    length = max(len(r), length)

for _ in range(length):
    for r in li:
        if r:
            answer += r.pop(0)

print(answer)