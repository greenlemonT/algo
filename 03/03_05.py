"""
행렬의 거듭제곱
N x N 정방행렬 A와 양의정수 b가 주어졌을떄 A행렬의 거듭제곱인 정방행렬 A^b을 출력하시오
단, 행렬의 원소는 항상 1,000으로 나눈 나머지 값만을 가진다. (거듭제곱의 중간 과정을 포함하여)
"""


# 행렬 곱셈 함수 정의
def multiply(A, B, N):
    tmp= [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += A[i][k] * B[k][j]
                tmp[i][j] %= 1000
    return tmp

# 분할 정복을 이용한 거듭제곱 함수 정의
def solution(A, b, N):
    if b == 1:
        return A
    elif b % 2 == 0:  # b가 짝수일 때
        a = solution(A, b//2, N)
        return multiply(a, a, N)
    else:  # b가 홀수일 때
        a = solution(A, b//2, N)
        return multiply(multiply(a, a, N), A, N)  # A * (A^(b//2)) * (A^(b//2))

# 입력 처리
N, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 거듭제곱 결과
result = solution(A, b, N)

# 결과 출력
for row in result:
    print(' '.join(map(str, row)))
