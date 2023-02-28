n=int(input())
stones=list(map(int,input().split()))

import functools

x=functools.reduce(lambda x,y:x^y,stones)

if x==0:
    print("No")
else:
    print("Yes")
