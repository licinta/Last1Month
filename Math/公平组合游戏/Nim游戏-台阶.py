n=int(input())
stones=list(map(int,input().split()))

import itertools,functools 
stones=itertools.compress(stones,[i%2 for i in range(1,n+1)])
if functools.reduce(lambda x,y:x^y,stones)==0:
    print("No")
else:
    print("Yes")
