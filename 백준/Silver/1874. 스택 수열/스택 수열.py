import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

nums = []  # 스택
result = []  # 결과
next_num = 1  # 다음으로 추가할 숫자

for target in arr:
    # 스택에 target까지 숫자를 추가
    while next_num <= target:
        nums.append(next_num)
        result.append("+")
        next_num += 1

    # 스택의 top과 target 비교
    if nums and nums[-1] == target:
        nums.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)

print("\n".join(result))
