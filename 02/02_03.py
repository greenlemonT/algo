def solution(n):
    answer = []

    while n != 1:
        answer.append(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    answer.append(1)
    answer_str = [str(num) for num in answer]

    return ' '.join(answer_str)

num=int(input())
print(solution(num))