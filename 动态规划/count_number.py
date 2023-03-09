from functools import lru_cache


def toInt(li):
    power = [10**i for i in range(len(li)-1, -1, -1)]
    ans = 0
    for i in range(len(li)):
        ans += li[i]*power[i]
    return ans


@lru_cache(None)
def count_nozero(li=(3, 2, 5), x=2):
    if len(li) == 0:
        return 0
    if li[0] > x:
        ans = 0
        ans += count_nozero(tuple([x]+[9 for i in range(len(li)-1)]), x)
        ans += count_nozero(li[1:], x)
        ans += (li[0]-x-1) * \
            count_nozero(tuple([9 for i in range(len(li)-1)]), x)
    if li[0] == x:
        ans = 0
        ans += toInt(li[1:])+1
        ans += li[0]*count_nozero(tuple([9 for i in range(len(li)-1)]), x)
        ans += count_nozero(li[1:], x)
    if li[0] < x:
        ans = 0
        ans += li[0]*count_nozero(tuple([9 for i in range(len(li)-1)]), x)
        ans += count_nozero(li[1:], x)
    # print(f'f({li},{x})={ans}')
    return ans


def func(x, y):
    from collections import Counter
    c = Counter()
    for i in range(x+1):
        c += Counter(str(i))
    return c[str(y)]


def count_zero(li=(3, 2, 5), x=0):
    if len(li) == 0:
        return 0
    ans = 0
    ans += count_nozero(li[1:], x)
    ans += (li[0]-1)*count_nozero(tuple([9 for i in range(len(li)-1)]),
                                  x)+count_zero(tuple([9 for i in range(len(li)-1)]), x)
    return ans


def toTuple(x):
    return tuple(map(int, list(str(x))))


def f(a, b, i):
    if not i:
        return count_zero(toTuple(b), i)-count_zero(toTuple(a), i)
    return count_nozero(toTuple(b), i)-count_nozero(toTuple(a), i)


a, b = 1, 1
a, b = map(int, input().split())
while a | b:
    if a > b:
        a, b = b, a
    for i in range(10):
        if a > 0:
            print(f(a-1, b, i), end=' ')
        else:
            if i == 0:
                print(count_zero(toTuple(b), 0), end=' ')
            else:
                print(count_nozero(toTuple(b), i), end=' ')
    print()
    a, b = map(int, input().split())
