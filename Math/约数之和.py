from collections import Counter
<<<<<<< HEAD
n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
    
def fun(x):
    c=Counter()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            while x%i==0:
                c[i]+=1
                x//=i
    if x>1:
        c[x]+=1
    return c
            
c=Counter()
for i in li:
    c+=fun(i)
##print(c)
##a=p1^x1 * p2^x2 * p3^x3... * pn^xn
##
=======

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))


def fun(x):
    c = Counter()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            while x % i == 0:
                c[i] += 1
                x //= i
    if x > 1:
        c[x] += 1
    return c


c = Counter()
for i in li:
    c += fun(i)
ans = 1
for i, j in c.items():
    ans *= 1 * (1 - i ** (j + 1)) // (1 - i)
    ans %= 1000000007
print(ans)
##print(c)
##a=p1^x1 * p2^x2
## p1^0 * p2^0 + p1^1 * p2^0 + p1^1 * p2^1 + p1^0 * p2^1
## (p1^0 + p1^1 + p1^2 + ... +p1^n) * (p2^0 + p2^1 + p2^2 + ... +p2^n)
>>>>>>> 06ec18d (Add files via upload)
