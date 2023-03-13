n = int(input())

graph = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
child = [[] for i in range(n)]
num = [0 for i in range(n)]
s = set()


def count(root):
    """
    count the node's number of sub-tree
    """
    s.add(root)
    ans = 1
    for i in graph[root]:
        if i not in s:
            ans += count(i)
            child[root].append(i)
    num[root] = ans
    return ans


count(0)

ans = 0xffffff
for i in range(n):
    upper = num[0]  # the upper tree
    temp = 0  # the branch sub-tree's maxium number
    for to in child[i]:
        upper -= num[to]
        temp = max(temp, num[to])
    ans = min(ans, max(temp, upper - 1))  # do not forget the deleted i node itself!
print(ans)
