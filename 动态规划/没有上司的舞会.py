import functools
from sys import setrecursionlimit

"""
goals: 9/12
"""
setrecursionlimit(10000005)


class node:
    def __init__(self, id):
        self.child = []
        self.id = id
        self.happiness = 0

    def set_child(self, nd):
        self.child.append(nd)

    def set_happiness(self, happiness):
        self.happiness = happiness


h = []
n = int(input())
tree = [node(i) for i in range(n)]

for i in range(n):
    tree[i].set_happiness(int(input()))

left = set()
right = set()
"""
the root only appear at the right,so the diff on set can work out to find the final root node.
"""
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[b - 1].set_child(tree[a - 1])
    left.add(a - 1), right.add(b - 1)
root = 0
if n > 1:
    right = right.difference(left)
    root = right.pop()

select, unselect = 1, 0
dp = [[0, 0] for i in range(n)]


@functools.lru_cache(None)
def dfs(root, do):
    """
    how much happiness can we get from the sub-tree if we do 'do' method on the tree[root].
    1
    2  3
    """
    if do == select:
        dp[root][do] = tree[root].happiness

    for child in tree[root].child:
        if do == select:
            dp[root][select] += dfs(child.id, unselect)
        else:
            dp[root][unselect] += max(dfs(child.id, select), dfs(child.id, unselect))
    return dp[root][do]


print(max(dfs(root, unselect), dfs(root, select)))
