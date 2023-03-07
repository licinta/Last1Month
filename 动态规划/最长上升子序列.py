from functools import lru_cache
n = int(input())
li = list(map(int, input().split()))


def f():
    dp = [1 for i in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            if li[j] > li[i]:
                dp[j] = max(dp[j], dp[i]+1)
    return max(dp)


print(f())
