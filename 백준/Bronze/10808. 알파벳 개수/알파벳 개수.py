s = input()

arr = [0] * 26

for word in s:
    arr[ord(word) - 97] += 1


any(print(s, end=' ') for s in arr)