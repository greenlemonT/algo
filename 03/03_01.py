
"""
이분탐색 재귀 알고리즘 구현
input:
n,m
n개의, 정렬되지않은정수
m개의 리스트에서 탐색하고자 하는 양의 정수
output:
m개의 줄에 이분탐색 결과
첫번쨰값은 location()함수 호출횟수
두번쨰값은 정렬된 리스트에서의 위치 인덱스
"""
def binary_search_recursive(array, target, start, end):
    global count
    if start > end:
        return None
    mid = (start + end) // 2
    count += 1
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)
    else:
        return binary_search_recursive(array, target, mid + 1, end)

N, M = map(int, input().split())
array = list(map(int, input().split()))
targets = list(map(int, input().split()))
array.sort()

for target in targets:
    count = 0
    result = binary_search_recursive(array, target, 0, N-1)
    if result == None:
        print(target,0)
    else:
        print(count,result + 1)
