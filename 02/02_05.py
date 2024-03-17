#하노이의탑
#n=하노이의개수,k=k번째 이동방향
def hanoi(n, src, via, dst):
    global moves
    global count
    if n == 1:
        moves.append((src, dst))
        count += 1
    else:
        hanoi(n-1, src, dst, via)
        moves.append((src, dst))
        count += 1
        hanoi(n-1, via, src, dst)
        count += 1

def solution(N, K):
    global moves
    global count
    moves = []
    count = 0
    hanoi(N, 'A', 'B', 'C')
    print(f'{moves[K-1][0]} -> {moves[K-1][1]}')
    print(f'{count}')

N, K = map(int, input().split())
solution(N, K)
