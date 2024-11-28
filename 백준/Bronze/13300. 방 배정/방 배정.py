n, k = map(int, input().split())

boys = []
girls = []

for _ in range(n):
	s, y = map(int, input().split())
	if s == 0:
		girls.append(y)
	else:
		boys.append(y)

def count_rooms(num, rooms):
	if num:
		rooms += num // k
		if num % k:
			rooms += 1
		else:
			rooms += 0
	return rooms

rooms = 0
for i in range(1, 7):
	boys_num = boys.count(i)
	girls_num = girls.count(i)
	rooms = count_rooms(boys_num, rooms)
	rooms = count_rooms(girls_num, rooms)

print(rooms)
