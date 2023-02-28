import copy
import itertools
import functools
from pprint import pprint
import heapq
def check(m):
    return m==[['1','1','1','1','1'] for i in range(5)]

def change(m,i,j):
    m=copy.deepcopy(m)
    m[i][j]=str(int(m[i][j])^1)
    if 0<=i-1<5:
        m[i-1][j]=str(int(m[i-1][j])^1)
    if 0<=i+1<5:
        m[i+1][j]=str(int(m[i+1][j])^1)
    if 0<=j-1<5:
        m[i][j-1]=str(int(m[i][j-1])^1)
    if 0<=j+1<5:
        m[i][j+1]=str(int(m[i][j+1])^1)
    return m
def toString(m):
    return ''.join([''.join(i) for i in m])

def bfs():
    d={}
    m=[['1','1','1','1','1'] for i in range(5)]
    d[toString(m)]=0
    for i in itertools.permutations([k for k in range(25)],6):
        cur=copy.deepcopy(m)
        for j in range(1,7):
            cur=change(cur,list(i)[j-1]//5,list(i)[j-1]%5)
            if toString(cur) not in d:
                d[toString(cur)]=0xffff
            d[toString(cur)]=min(d[toString(cur)],j)
    return d
            

n=int(input())
d=bfs()
print('finish')
for i in range(n):
    m=[]
    if i:
        input()
    for j in range(5):
        m.append(list(input()))
    
    if m in d:
        print(d[m])
    else:
        print(-1)

