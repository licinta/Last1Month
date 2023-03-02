import heapq
n = int(input())
li = list(map(int, input().split()))
ans = 0
li.sort()
# print(li)
for i in range(n):
    ans += li[i]*(n-1-i)
print(ans)
