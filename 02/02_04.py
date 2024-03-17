#가장 긴 콜라츠 수열 출력
#input=n,m
#output=첫째 줄에 N보다 크거나 같고, M보다 작거나 같은 수 중에서 가장 긴 콜라츠 수열을 가진 수 K와 K의 콜라츠 수열 길이를 출력한다.
#둘째 줄에 K의 콜라츠 수열을 출력한다.
#단, 콜라츠 수열의 최장 길이가 같은 수가 여러 개 있으면, 그 중 가장 큰 수를 K로 정한다.
def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

n, m = map(int, input().split())
max_length = 0
result_number = 0

for number in range(n, m+1):
    current_length = collatz_length(number)
    if current_length >= max_length:
        max_length = current_length
        result_number = number

print(result_number, max_length-1)
print(*collatz(result_number))
