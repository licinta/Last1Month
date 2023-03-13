n = int(input())

graph = [[] for i in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    graph[a - 1].append(b)
    graph[b - 1].append(a)


