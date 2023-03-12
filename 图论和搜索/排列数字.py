n = int(input())

q = []


def dfs(li, i=0):
    if i == len(li) - 1:
        q.append(li)
        return

    for start in range(i, len(li)):
        copy = li[:]
        copy[start], copy[i] = copy[i], copy[start]
        dfs(copy, i + 1)


dfs([i for i in range(1, n + 1)])
for i in sorted(q):
    print(*i)
