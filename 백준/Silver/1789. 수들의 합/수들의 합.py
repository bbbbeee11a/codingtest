n = int(input())

i = 1
cnt = 0

while n >= 0:
	n -= i
	cnt += 1
	i += 1

print(cnt - 1)