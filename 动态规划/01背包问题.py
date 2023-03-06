import functools
import sys
sys.setrecursionlimit(100005)

n, m = map(int, input().split())
goods = []
for i in range(n):
    goods.append(list(map(int, input().split())))


@functools.lru_cache(None)
def knapsack(i, v):
    if i == len(goods):
        return 0
    if v < 0:
        return -10000000000
    if v >= goods[i][0]:
        return max(knapsack(i+1, v-goods[i][0])+goods[i][1], knapsack(i+1, v))

    return knapsack(i+1, v)


print(knapsack(0, m))
