def solution(arr):
    answer = []
    prev = -1
    
    for k in arr:
        if k != prev:
            answer.append(k)
        prev = k
        
    return answer