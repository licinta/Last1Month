import math
n=int(input())
def qmi(a,b,c):
    ans=1
    while b:
        if b&1==1:
            ans*=a
            ans%=c
        a*=a
        a%=c
        b>>=1
    return ans

for i in range(n):
    a,b=map(int,input().split())
    if math.gcd(a,b)==1:
        print(qmi(a,b-2,b))
    else:
        print("impossible")

