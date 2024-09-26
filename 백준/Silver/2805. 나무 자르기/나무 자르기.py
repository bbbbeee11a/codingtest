import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().strip().split()))


def get_tree(max_height, trees):
    total = 0
    for tree in trees:
        if tree > max_height:
            total += tree - max_height
    return total


def get_height(M, trees):
    l = 0
    h = max(trees)
    result = 0
    
    while l <= h:
        mid = (l + h) // 2
        woods = get_tree(mid, trees)
        
        if woods >= M:
            result = mid
            l = mid + 1
        else:
            h = mid - 1

    return result

print(get_height(M, trees))