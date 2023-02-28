
n, m = map(int, input().split())
s = {}


def fa(x):
    if x not in s:
        s[x] = x
    if s[x] == x:
        return x
    s[x] = fa(s[x])
    return s[x]


def uni(a, b):
    f_a, f_b = fa(a), fa(b)
    s[f_a] = f_b


for i in range(m):
    a, b, c = input().split()
    if a == 'M':
        uni(b, c)
    else:
        print(fa(b) == fa(c))
