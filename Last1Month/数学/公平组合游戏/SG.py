import functools


def mex(t):
    if not t:
        return 0
    s = set(t)
    for i in range(0, len(t)+2):
        if i not in s:
            return i


@functools.lru_cache(None)
def sg(cur, method):
    if cur == 0:
        return 0
    return mex([sg(cur-i, method) for i in method if i <= cur])


print(sg(10, (2, 5)))
