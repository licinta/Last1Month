from collections import Counter
def eular(x):
    ans=x
    c=Counter()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            while x%i==0:
                x//=i
                c[i]+=1
    if x>1:
        c[x]+=1
    for i,j in c.items():
        ans*=i-1
        ans//=i
    return ans
n=int(input())
for i in range(n):
    print(eular(int(input())))
