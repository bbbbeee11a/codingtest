import sys

input = sys.stdin.readline

stack = list()

for _ in range(int(input())):
	request = list(input().split())
	order = request[0]

	if order == "push":
		stack.append(request[1])

	elif order == "pop":
		if not stack:
			print(-1)
		else:
			top = stack.pop()
			print(top)

	elif order == "size":
		print(len(stack))

	elif order == "empty":
		print(0 if stack else 1)

	elif order == "top":
		print(stack[-1] if stack else -1)

	else:
		print("error!")
