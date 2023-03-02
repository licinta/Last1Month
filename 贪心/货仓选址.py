n = int(input())
li = list(map(int, input().split()))
li.sort()
ans = 0
for i in range(n//2):
    ans += li[-1-i]-li[i]
print(ans)
