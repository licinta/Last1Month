n = int(input())
s1 = input()
m = int(input())
s2 = input()

dp = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(m+1):
    dp[0][i] = i
for i in range(n+1):
    dp[i][0] = i
for i in range(n):
    for j in range(m):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j]
        else:
            dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j])+1
print(dp[n][m])
