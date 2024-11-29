from collections import Counter

a = Counter(input())
b = Counter(input())

if a == b:
	print(0)
else:
	print((a-b).total() + (b-a).total())