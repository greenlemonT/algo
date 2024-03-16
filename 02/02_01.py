def fun(n):
    cnt = 0
    for i in range(1, 4*n+1, 2):
        cnt += n
    return cnt

num=int(input())
print(fun(num))