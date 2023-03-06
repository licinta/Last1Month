import functools
import sys
sys.setrecursionlimit(1000005)
n, m = map(int, input().split())
wei, val = [], []
for i in range(n):
    a, b = map(int, input().split())
    wei.append(a)
    val.append(b)


@functools.lru_cache(None)
def f(item, space):
    if item == -1:
        return 0
    if space < 0:
        return -10000000
    return max([f(item-1, space-k*wei[item])+k*val[item] for k in range(space//wei[item]+1)])


print(f(n-1, m))
