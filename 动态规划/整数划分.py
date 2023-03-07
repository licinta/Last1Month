# n=int(input())
n=5
inf=1000000007
def f(x,i):
    if x==0:
        return 1
    ans=0
    for k in range(1,min(i,x)+1):
        ans+=f(x-k,k)
        ans%=inf
    return ans

print(f(n,n))
