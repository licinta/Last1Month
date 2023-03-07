from bisect import bisect_left
n = int(input())
li = list(map(int, input().split()))

ans = [float('inf') for i in range(n+1)]
for i in li:
    ans[bisect_left(ans, i)] = i
print(ans.index(float('inf')))
