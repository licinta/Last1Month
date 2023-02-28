n=int(input())

def qmi(a,b,c):
    base=a
    ans=1
    while b:
        if b&1:
            ans*=base
            ans%=c
        base*=base
        base%=c
        b>>=1
    return ans*base


for _ in range(n):
    a,b,c=map(int,input().split())
    print(qmi(a,b,c))
