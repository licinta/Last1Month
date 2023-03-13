from heapq import *

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])


def dijkstra(graph, n, start, end):
    q = [[0xfffffff, start]]
    s = set()  # has been ensurred
    dis = [0xfffffff for i in range(n + 1)]
    dis[start] = 0
    while q:
        distance, cur = heappop(q)
        for to, wei in graph[cur]:
            if to not in s and dis[cur] + wei < dis[to]:
                dis[to] = dis[cur] + wei
                s.add(to)
                heappush(q, [dis[to], to])
    return dis[end] if dis[end] != 0xfffffff else -1


print(dijkstra(graph, n, 1, n))
