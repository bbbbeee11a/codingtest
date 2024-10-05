import sys
from collections import defaultdict
import math

input = sys.stdin.readline

def sol(nums):
    num_dict = defaultdict(int)
    for num in nums:
        count = 0
        for alpha in num:
            if alpha.isupper():
                count += 1
        #num_dict[num.lower()] = count
        num_dict[num] = count

    li = list()
    for k, v in num_dict.items():
        li.append((''.join(sorted(k.lower())), v))
    # print(li)
    x_li = []
    answer_li = []
    for x in li:
        if x not in x_li:
            x_li.append(x)
        else:
            answer_li.append(x)

    # print(answer_li)
    if len(answer_li) == len(li) - 1:
        return math.comb(len(li), 2)
    else:
        return len(answer_li)

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    nums = list(input().split())
    answer = sol(nums)
    print(answer)
