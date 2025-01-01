import sys

input = sys.stdin.readline

cal = []
cur = 0

for i in range(int(input())):
	num = int(input())
	if num:
		cal.insert(cur, num)
		cur += 1

	else:
		cur -= 1
		cal[cur] = 0


print(sum(cal))
