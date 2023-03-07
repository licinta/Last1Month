from functools import lru_cache
import itertools

n = int(input())
st = list(map(int, input().split()))
pref = [0]+list(itertools.accumulate(st))


@lru_cache(None)
def f(i, j):
    if i == j:
        return 0
    return min([f(i, k)+f(k+1, j)+pref[j+1]-pref[i] for k in range(i, j)])


print(f(0, n-1))
