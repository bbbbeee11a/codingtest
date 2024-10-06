import sys

input = sys.stdin.readline

def sol(arr):
    dp_asc = [1] * (N)
    dp_desc = [1] * (N)
    rev_arr = arr.copy()[::-1]

    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp_asc[i] = max(dp_asc[i], dp_asc[j] + 1)


    for i in range(N):
        for j in range(i):
            if rev_arr[i] > rev_arr[j]:
                dp_desc[i] = max(dp_desc[i], dp_desc[j] + 1)
    
    answer = 0
    for i in range(N):
        tmp = dp_asc[i] + dp_desc[N - 1 - i] - 1
        answer = max(tmp, answer)
        
    return answer


N = int(input())
A = list(map(int, input().split()))

print(sol(A))
