# a*x=b %m
# a*x + m*y = b
n = int(input())


def exgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, s, t = exgcd(b, a % b)
    return g, t, s-a//b*t


for _ in range(n):
    a, b, m = map(int, input().split())
    gcd, s, t = exgcd(a, m)
    if b % gcd:
        print("impossible")
    else:
        # 答案要求必须在int范围内，只需要对m取个模就能满足
        print(s*(b//gcd) % m)
