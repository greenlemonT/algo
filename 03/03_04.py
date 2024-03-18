"""
퀵정렬, 분할 알고리즘
input:
첫째 줄에 리스트의 원소 개수 N이 주어진다.
둘째 줄에 정렬되지 않은 N개의 양의 정수가 주어진다.
output:
첫째 줄에 주어진 리스트를 퀵 정렬로 정렬하여 오름차순으로 출력한다.
둘째 줄에 swap 연산의 총 실행 횟수출력
"""

N = int(input())
S = list(map(int, input().split()))
cnt = 0

def quick_sort(low, high):
    global cnt
    if low < high:
        pivotpoint = partition(low, high)
        quick_sort(low, pivotpoint-1)
        quick_sort(pivotpoint+1, high)

def partition(low, high):
    global cnt
    pivotitem = S[low]
    j = low
    for i in range(low + 1, high + 1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]
            cnt += 1

    pivotpoint = j
    S[low], S[pivotpoint] = S[pivotpoint], S[low]
    cnt += 1
    return pivotpoint

quick_sort(0, N-1)
print(" ".join(map(str, S)))
print(cnt)
