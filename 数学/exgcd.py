n=int(input())
def exgcd(a,b):
    if b==0:
        return a,1,0
    _gcd,s,t=exgcd(b,a%b)
    return _gcd,t,s-a//b*t

for _ in range(n):
    a,b=map(int,input().split())
    print(*exgcd(a,b,)[1:])
    
