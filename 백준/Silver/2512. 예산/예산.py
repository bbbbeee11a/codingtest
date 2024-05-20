# 입력
n = int(input())
requests = list(map(int, input().split()))
budget = int(input())


# 상한액이 upper_bound일 때 필요한 예산을 계산하는 함수
def calculate_needed_budget(upper_bound: int) -> int:
    needed_budget = 0
    for request in requests:
        needed_budget += min(request, upper_bound)

    return needed_budget


# 이분 탐색을 수행하는 메인 로직
low = 0
high = max(requests)
optimum = -1

while low <= high:
    mid = (low + high) // 2

    if calculate_needed_budget(mid) <= budget:
        optimum = mid
        low = mid + 1
    else:
        high = mid - 1

ans = -1
for request in requests:
    given = min(request, optimum)
    ans = max(ans, given)

print(ans)