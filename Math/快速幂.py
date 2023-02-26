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
    a,b,c=map(int,input().split())
    print(qmi(a,b,c))
