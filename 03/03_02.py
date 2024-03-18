#합병정렬 알고리즘1
def merge(U, V):
    S = []
    i = j = 0

    while i < len(U) and j < len(V):
        if U[i] < V[j]:
            S.append(U[i])
            i += 1
        else:
            S.append(V[j])
            j += 1

    # 남은 요소들 추가하기
    S += U[i:] + V[j:]

    return S

def mergesort(S):
    n = len(S)
    if n <= 1:
        return S

    mid = n // 2
    left = mergesort(S[:mid])
    right = mergesort(S[mid:])

    # 병합 과정에서 비교 횟수 업데이트
    cnt[0] += len(left) + len(right)

    return merge(left, right)

N = int(input())
S = list(map(int, input().split()))
cnt = [0]  # 비교 횟수를 담을 리스트, 전역 변수 사용을 줄이기 위해

sorted_S = mergesort(S)

print(' '.join(map(str, sorted_S)))
print(cnt[0])
