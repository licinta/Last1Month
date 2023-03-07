from pprint import pprint
from functools import lru_cache
n = int(input())
trig = []
for i in range(n):
    trig.append(list(map(int, input().split())))

# pprint(trig)


@lru_cache(None)
def f(i, j):
    if i == n:
        return 0
    return max(f(i+1, j), f(i+1, j+1))+trig[i][j]


print(f(0, 0))
