n=int(input())

li=list(map(int,input().split()))

p=list(zip(li,[i for i in range(1,n+1)]))

p.sort(key=lambda x:x[0])

ans=0
it=0
for i,j in p:
    print(j,end=' ')
    ans+=i*(n-1-it)
    it+=1
print()
print("%.2f"%(ans/n))
