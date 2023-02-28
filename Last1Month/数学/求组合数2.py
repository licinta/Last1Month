# a!*b!/(a-b)!
# a*x=1(mod 1000000007)
# 打表2~100000的逆元和积

def fiman(a, p):
    mod = p
    ans = 1
    p -= 2
    while p:
        if p & 1:
            ans *= a
            ans %= mod
        p >>= 1
        a *= a
        a %= mod
    return ans


fact = [1 for i in range(100005)]
mod = 1000000007
for i in range(2, 100005):
    fact[i] = (fact[i-1]*i) % mod


def Comb(a, b):
    return fact[a]*fiman(fact[b],mod)*fiman(fact[a-b],mod)%mod

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(Comb(a, b))
