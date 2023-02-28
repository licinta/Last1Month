def fiman(a, p):
    b = p-2
    ans = 1
    while b:
        if b & 1:
            ans *= a
            ans %= p
        a *= a
        a %= p
        b >>= 1
    return ans


def Comb(a, b, p):
    ## python version>=3.8
    # import math
    # return math.comb(a, b) % p
    if a < b:
        return 0
    fact = [1 for i in range(100005)]
    for i in range(2, max(a, b)+1):
        fact[i] = (fact[i-1]*i) % p

    return fact[a]*fiman(fact[b], p)*fiman(fact[a-b], p) % p


def lucas(a, b, p):
    if b == 0:
        return 1
    if b > a:
        return 0
    if a < p and b < p:
        return Comb(a, b, p)
    return lucas(a//p, b//p, p)*Comb(a % p, b % p, p) % p


n = int(input())

for i in range(n):
    a, b, p = map(int, input().split())
    print(lucas(a, b, p))
