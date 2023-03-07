import functools
from pprint import pprint
n, m = map(int, input().split())
group = []

for i in range(n):
    x = int(input())
    temp = []
    for j in range(x):
        temp.append(list(map(int, input().split())))
    group.append(temp)

pprint(group)


@functools.lru_cache(None)
def knapsack(i, v):
    if i == -1 and v >= 0:
        return 0
    if v < 0:
        return -100000000
    temp = max(knapsack(i-1, v),
               max([knapsack(i-1, v-wei)+val for wei, val in group[i]]))
    # print(f"f({i},{v})={temp}")
    return temp


print(knapsack(n-1, m))
