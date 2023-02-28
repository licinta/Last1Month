n = int(input())
p = 1000000007
"""
catland = [0 for i in range(n+1)]
catland[0] = 1
for i in range(1, n+1):
    for j in range(i):
        catland[i] += catland[j]*catland[i-1-j]
        catland[i] %= p
print(catland[n])
"""
def qmi(a,b):
    ans=1
    while b:
        if b&1:
            ans*=a
            ans%=p
        b>>=1
        a*=a
        a%=p
    return ans

def Comb(a,b):
    ans=1
    for i in range(a,a-b,-1):
        ans*=i
        ans%=p
    for i in range(1,b+1):
        ans*=qmi(i,p-2)
        ans%=p
    return ans

print((Comb(2*n,n)-Comb(2*n,n-1))%p)
