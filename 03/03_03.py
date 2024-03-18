#합병정렬알고리즘2
def merge2(low, mid, high):
    global S, cnt
    i, j = low, mid + 1
    U = []

    # 배열의 두 부분을 비교하며 정렬하여 U에 저장
    while i <= mid and j <= high:
        cnt += 1  # 비교 연산 카운트
        if S[i] < S[j]:
            U.append(S[i])
            i += 1
        else:
            U.append(S[j])
            j += 1

    # 남아 있는 요소들 처리
    U.extend(S[i:mid+1])
    U.extend(S[j:high+1])

    # 복사
    S[low:high+1] = U

def merge_sort(low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        merge2(low, mid, high)

N = int(input().strip())
S = list(map(int, input().strip().split()))
cnt = 0

merge_sort(0, N-1)

print(' '.join(map(str, S)))
print(cnt)
