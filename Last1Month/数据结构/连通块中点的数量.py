n, m = map(int, input().split())
s = {}
cnt = {}


def fa(x):
    if x not in s:
        s[x] = x
        cnt[x] = 1
    if s[x] == x:
        return x
    s[x] = fa(s[x])
    cnt[s[x]] = cnt[x]+1
    return s[x]


def uni(a, b):
    f_a, f_b = fa(a), fa(b)
    s[f_a] = f_b
    cnt[f_a] += cnt[f_b]


for i in range(m):
    li = input().split()
    if len(li)==2:
        print(cnt[fa(li[1])])
    else:
        if li[0]=='C':
            uni(li[1],li[2])
        else:
            if fa(li[1])==fa(li[2]):
                print("Yes")
            else:
                print("No")
