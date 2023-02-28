n=int(input())
def fun(x):
    """
    if a number can be pri p1^a * p2^b,
    extremely, a=b=1 , and obiviously sqrt(num)>=p1,
    so when the loop is ended, the remaining must be a prime num.
    """
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            j=0
            while x%i==0:
                x//=i
                j+=1
            print(i,j)
    if x-1:
        print(x,1)
    print()
for _ in range(n):
    x=int(input())
    fun(x)
