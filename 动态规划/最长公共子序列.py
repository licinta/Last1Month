import functools
import sys
sys.setrecursionlimite(10005)
n, m = map(int, input().split())

s1, s2 = input(), input()


@functools.lru_cache()
def f(i, j):
    if i == -1 or j == -1:
        return 0
    if s1[i] == s2[j]:
        return f(i-1, j-1)+1
    return max(f(i-1, j), f(i, j-1), f(i-1, j-1))


def g():
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], dp[i][j])
    return dp[-1][-1]


print(g())
print(f(len(s1)-1, len(s2)-1))
