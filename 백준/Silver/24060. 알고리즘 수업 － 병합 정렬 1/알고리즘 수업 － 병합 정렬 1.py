import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0  # 병합 과정에서 저장된 값의 순서를 카운트
result = -1  # K번째 값을 저장할 변수


def merge(A, p, q, r):
    global count, result

    i, j = p, q + 1
    tmp = []

    # 두 부분 배열을 병합
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    # 남아 있는 요소를 추가
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1

    # 병합된 결과를 원본 배열에 복사
    for i in range(len(tmp)):
        A[p + i] = tmp[i]
        count += 1  # 저장된 값 카운트
        if count == K:  # K번째 값일 경우 저장
            result = tmp[i]


def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


merge_sort(A, 0, N - 1)
print(result if result != -1 else -1)
