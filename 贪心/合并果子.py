import heapq
n = int(input())
li = list(map(int, input().split()))
heapq.heapify(li)
ans = 0
while len(li) > 1:
    a, b = heapq.heappop(li), heapq.heappop(li)
    ans += a+b
    heapq.heappush(li, a+b)

# ans += heapq.heappop(li)
print(ans)
