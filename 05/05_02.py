#05_02
#이항계수를 구하는 동적계획법 알고리즘
#태뷸레이션
def binom(n, k):
    if k == 0 or k == n:
        return 1
    DP = [1] * (n+1)
    for i in range(1, n+1):
        DP[i] = 1
        for j in range(i-1, 0, -1):
            DP[j] = (DP[j] + DP[j-1]) % 10007
    return DP[k]

n, k = map(int, input().split())
print(binom(n, k))