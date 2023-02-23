from collections import Counter
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
