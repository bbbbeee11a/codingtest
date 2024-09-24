import sys

# 한 번에 모든 입력을 받아 처리
input = sys.stdin.read
data = input().splitlines()

# N과 M 입력 받기
N, M = map(int, data[0].split())

# 집합 A와 B 생성
A = set(data[1:N+1])
B = set(data[N+1:N+M+1])

# 교집합 결과 구하기
answer = sorted(A & B)

# 출력
sys.stdout.write(f"{len(answer)}\n" + "\n".join(answer) + "\n")