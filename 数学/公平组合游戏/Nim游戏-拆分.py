
"""
每次取出一堆而放入两堆更小者(可以为0)
"""
import functools
n = int(input())

stones = list(map(int, input().split()))


def mex(s):
    if not s:
        return 0
    for i in range(len(s)+2):
        if i not in s:
            return i


@functools.lru_cache(None)
def sg(x):
    if x == 0:
        return 0
    s = set()
    for i in range(x):
        for j in range(i+1):
            s.add(sg(i) ^ sg(j))
    return mex(s)


stones=[sg(i) for i in stones]
if functools.reduce(lambda x,y:x^y,stones)==0:
    print("No")
else:
    print("Yes")
