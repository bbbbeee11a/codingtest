import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().strip().split()))


# max_height 기준으로 얻을 수 있는 나무 길이 계산
def get_tree(max_height, trees):
    total = 0
    for tree in trees:
        if tree > max_height:
            total += tree - max_height
    return total


# 이진 탐색으로 최대 절단 높이 찾기
def get_height(M, trees):
    l = 0
    h = max(trees)
    result = 0
    
    while l <= h:
        mid = (l + h) // 2
        wood = get_tree(mid, trees)  # mid 기준으로 나무 길이 계산
        
        if wood >= M:  # 필요한 나무 길이보다 크거나 같으면 더 높은 절단 가능
            result = mid  # 최적 해 후보 갱신
            l = mid + 1
        else:  # 필요한 나무 길이보다 작으면 더 낮게 절단해야 함
            h = mid - 1
    
    return result

print(get_height(M, trees))