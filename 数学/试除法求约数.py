import itertools as it
import functools as ft
n=int(input())
def fun(x):
    fact=[1]
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            while x%i==0:
                x//=i
                fact+=[i]
    if x-1:
        fact+=[x]
    s=set([])
    for i in range(1,len(fact)+1):
        for j in it.combinations(fact,i):
            s.add(list(it.accumulate(j,lambda x,y:x*y))[-1])
    print(*sorted(s))

for i in range(n):
    fun(int(input()))
