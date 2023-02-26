n=int(input())
prime=[]
phi=[0 for i in range(n+1)]
num=[0 for i in range(n+1)]
phi[1]=1
num[0]=num[1]=1
for i in range(2,n+1):
    if num[i]==0:
        phi[i]=i-1
        prime.append(i)

    for j in prime:
        if j*i>n:break
        num[j*i]=1
        if i%j==0:
            phi[i*j]=phi[i]*j
            break 
        phi[i*j]=phi[i]*(j-1)

print(sum(phi))
    


