def base(n, x):
    ans = 0
    for i in range(n + 1):
        ans += str(i).count(str(x))
    return ans


def base_0(n, x):
    # to calc zero number
    ans = 0
    for i in range(n + 1):
        ans += str(i).rjust(len(str(n)), '0').count(str(x))
    return ans


def toInt(li):
    return int(''.join(map(str, li)))


def g(li, x):
    if len(li) == 1:
        return int(li[0] >= x)
    ans = 0
    ans += li[0] * g([9 for i in range(len(li) - 1)], x)
    ans += int(li[0] > x) * (10 ** (len(li) - 1))
    ans += int(li[0] == x) * (1 + int(''.join(map(str, li[1:]))))
    ans += g(li[1:], x)
    return ans


def z(li, x=0):
    if len(li) == 1:
        return 1
    ans = 0
    ans += z([9 for i in range(len(li) - 1)], x)
    ans += (li[0] - 1) * g([9 for i in range(len(li) - 1)], 0)
    ans += int(li[0] == 0) * toInt(li[1:]) + g(li[1:], 0)
    return ans


def wrap(f, n, x):
    return f(list(map(int, list(str(n)))), x)


func = [z, g]

a, b = map(int, input().split())
while a | b != 0:
    for i in range(10):
        print(wrap(func[int(i != 0)], max(a, b), i) - wrap(func[int(i != 0)], min(a, b) - 1, i), end=' ')
    print()
    a, b = map(int, input().split())
