#플로이드 알고리즘 + path출력
#행렬출력시 공백제거 ^^

INF = 999

def floyd(n, W, D):
    for i in range(1, n+1):
        for j in range(1, n+1):
            D[i][j] = W[i][j]
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])

def floyd2(n, W, D, P):
    for i in range(1, n+1):
        for j in range(1, n+1):
            D[i][j] = W[i][j]
            P[i][j] = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = k

def path(P, u, v, p):
    k = P[u][v]
    if k != 0:
        path(P, u, k, p)
        p.append(k)
        path(P, k, v, p)

n, m = map(int, input().split())
graph = [[INF if i != j else 0 for j in range(n+1)] for i in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w

T = int(input())
queries = [list(map(int, input().split())) for _ in range(T)]

D = [[INF for _ in range(n+1)] for _ in range(n+1)]
P = [[0 for _ in range(n+1)] for _ in range(n+1)]

floyd2(n, graph, D, P)

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n:
            print(D[i][j], end="")
        else:
            print(D[i][j], end=" ")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == n:
            print(P[i][j], end="")
        else:
            print(P[i][j], end=" ")
    print()


for u, v in queries:
    if D[u][v] == INF:
        print("NONE")
    else:
        print(u, end=" ")
        tmp = []
        path(P, u, v, tmp)
        for node in tmp:
            print(node, end=" ")
        print(v)
