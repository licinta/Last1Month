n=int(input())

dp=[0 for i in range(100)]
dp[1]=1
for i in range(2,n):
    dp[i]=dp[i-2]+dp[i-1]

for i in range(n):
    print(dp[i],end=' ')
