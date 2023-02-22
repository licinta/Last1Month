n=int(input())

def ais(n):
    prime=[0 for i in range(n+1)]
    ans=0
    prime[0]=prime[1]=1
    for i in range(2,n+1):
        if not prime[i]:
            ans+=1
            for j in range(i<<1,n+1,i):
                prime[j]=1
    print(ans)

ais(n)
