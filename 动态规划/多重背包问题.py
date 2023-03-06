from math import log2
n, m = map(int, input().split())
wei, val = [], []
for i in range(n):
    a, b, c = map(int, input().split())
    for t in range(int(log2(c))):
        t1, t2 = a*(2**t), b*(2**t)
        wei.append(t1)
        val.append(t2)
        c -= 2**t
    t1, t2 = c*a, c*b
    wei.append(t1)
    val.append(t2)


dp = [0 for i in range(m+1)]

print(m, len(wei))
for i in range(len(wei)):
    for j in range(m, wei[i]-1, -1):
        dp[j] = max(dp[j], dp[j-wei[i]]+val[i])
print(dp[-1])
