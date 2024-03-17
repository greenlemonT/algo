#시간복잡도 줄이기
"""
#include <bits/stdc++.h>
using namespace std;

typedef long long long_t;

long_t fun(long_t n) {
    if (n == 0)
        return 1;
    else {
        long_t s = 0;
        for (int i=1; i<=8; i++)
            s += fun(n/4);
        return s;
    }
}

int main() {
    long_t n;
    scanf("%lld", &n);
    printf("%lld", fun(n));
}
"""
def fun(n):
    if n == 0:
        return 1
    else:
        return 8 * fun(n//4)

n = int(input())
print(fun(n))

