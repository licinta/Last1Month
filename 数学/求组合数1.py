import functools
import itertools
import sys
sys.setrecursionlimit(int(1e6))


@functools.lru_cache(None)
def Comb(a, b):
    if b > a//2:
        # 细节优化
        return Comb(a, a-b)
    if a <= b:
        return 1
    if b == 0:
        return 1
    return (Comb(a-1, b-1)+Comb(a-1, b)) % 1000000007


# print(Comb(5,2))
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(Comb(a, b))
