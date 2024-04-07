#05_01
#이항계수를 구하는 재귀를 이용한 메모이제이션

#재귀호출의 범위 늘려줘야함!
import sys
sys.setrecursionlimit(10**6)

# 메모이제이션을 위한 DP 테이블 초기화
DP = [[-1 for _ in range(1001)] for _ in range(1001)]

def bin(n, k):
    global DP
    global cnt
    cnt += 1

    # 그전꺼 처리
    if k == 0 or k == n:
        DP[n][k] = 1
    # 아직 계산되지 않은 경우
    elif DP[n][k] == -1:
        DP[n][k] = (bin(n-1, k) + bin(n-1, k-1)) % 10007

    return DP[n][k]

n, k = map(int, input().split())
cnt = 0
print(bin(n, k))
print(cnt)
