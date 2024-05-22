N, T = tuple(map(int, input().split()))
A = list(map(int, input().split()))

def needed_num_operation(x: int) -> int:
    # 차이를 x 이하로 만들기 위해 필요한 연산(1을 감소시키는)의 횟수를 구합니다.

    B = [A[i] for i in range(N)]
    num_operations = 0

    # 왼쪽 <<< 오른쪽일 때 왼쪽 -> 오른쪽 연산
    for i in range(N - 1):
        if B[i + 1] - B[i] > x:
            num_operations += B[i + 1] - (B[i] + x)
            B[i + 1] = B[i] + x

    # 왼쪽 >>> 오른쪽일 때 오른쪽 -> 왼쪽 연산
    for i in range(N - 1, 0, -1):
        if B[i - 1] - B[i] > x:
            num_operations += B[i - 1] - (B[i] + x)
            B[i - 1] = B[i] + x

    return num_operations


low = 0
high = int(1e9)
answer = -1

while low <= high:
    mid = (low + high) // 2
    if needed_num_operation(mid) <= T:
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

for i in range(N - 1):
    if A[i + 1] - A[i] > answer:
        A[i + 1] = A[i] + answer

for i in range(N - 1, 0, -1):
    if A[i - 1] - A[i] > answer:
        A[i - 1] = A[i] + answer

print(" ".join(list(map(str, A))))
