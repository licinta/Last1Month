n,m=map(int,input().split())
prime=list(map(int,input().split()))

ans=0
import itertools
import functools
for i in range(1,m+1):
    for j in itertools.combinations(prime,i):
        ans+=n//functools.reduce(lambda x,y:x*y , j)*(-1)**(i-1)
print(ans)

