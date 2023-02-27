u=int(input())
A,M=[],[]
for i in range(n):
    m,a=map(int,input().split())
    A.append(a)
    M.append(m)
from ../Math/exCRT.py import exCRT
crt=exCRT(A,M)
print(crt.calc())
