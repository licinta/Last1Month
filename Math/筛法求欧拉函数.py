n=int(input())
prime=[]
num=[0 for i in range(n+1)]
num[1]=num[0]=1
phi=[0 for i in range(n+1)]
phi[1]=1
for i in range(2,n+1):
    if num[i]==0:
        prime.append(i)
        phi[i]=i-1

    for j in range(len(prime)):
        if prime[j]*i>n:break
        num[prime[j]*i]=1
        if i%prime[j]==0:
            phi[prime[j]*i]=phi[i]*prime[j]
            break
        phi[prime[j]*i]=phi[i]*(prime[j]-1)

print(sum(phi))
""" 
           phi(a)*phi(b)*gcd(a,b)
phi(ab) = ------------------------
               phi(gcd(a,b))
"""


