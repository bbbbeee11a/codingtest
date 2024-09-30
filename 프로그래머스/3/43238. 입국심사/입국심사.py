def solution(n, times):
    # 가능한 최솟값과 최댓값을 left와 right으로 설정
    left = 1
    right = max(times) * n

    # 이분탐색 진행
    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            # 해당 심사대에서 주어진 시간동안 심사받은 사람 수 더하기
            people += mid // time

            # n명보다 많이 심사하면 break
            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer