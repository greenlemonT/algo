#05_04
#삼각형의 최대경로
#공백 !!!!!!!!!!!!! -_-

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

path = [[0] * N for _ in range(N)]

for i in range(N):
    path[N-1][i] = graph[N-1][i]

for i in range(N-2, -1, -1):
    for j in range(i+1):
        if path[i+1][j] > path[i+1][j+1]:
            path[i][j] = graph[i][j] + path[i+1][j]
        else:
            path[i][j] = graph[i][j] + path[i+1][j+1]

print(path[0][0])

row, col = 0, 0
print(graph[row][col], end=' ')
for i in range(1, N):
    if col < N-1 and path[i][col] < path[i][col+1]:
        col += 1
    print(graph[i][col], end=' ')