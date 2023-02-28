def exgcd(a,b):
    if b==0:
        return a,1,0
    gcd,s,t=exgcd(b,a%b)
    return gcd,t,s-a//b*t



n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(*exgcd(a,b)[1:])
