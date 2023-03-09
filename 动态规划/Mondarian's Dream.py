from functools import lru_cache

def brk(temp):
    f = False
    l,r=0,0
    while l<len(temp):
        if temp[l]=='0':
            r=l
            while r<len(temp) and temp[r]=='0':
                r+=1
            count=r-l
            if count%2==1:
                f=True
                break
            else :
                l=r
        else:
            l+=1

    return f

@lru_cache(None)
def Mondarian(a, b):
    """
    the number of bricks which sticked out from the i-1-th column to i-th column
    initials:
        dp[0][0]=1
        the 0-th column has no bricks which begins at the front one column
    return:
        dp[b][0]
        all results must accord a state where no brick stick out fron the b-1-th column, as the b-1th is the last one column.
    """
    dp = [[0 for i in range(1 << a)] for j in range(b+1)]
    dp[0][0] = 1
    for column in range(1, b+1):
        for i in range(1 << a):
            if dp[column-1][i]==0:# to cut down nosense calculation
                continue
            for j in range(1 << a):
                temp = i & j
                if temp != 0:  # the brick has a maxium length of 2
                    continue
                temp = i | j
                temp = str(bin(temp))[2:].rjust(a,'0')

                if brk(temp):  # no odd interval was permitted to appear in all proper state.
                    continue

                dp[column][j] += dp[column-1][i]
    return dp[b][0]


# print(Mondarian(2, 4))

if __name__=="__main__":
    a,b=map(int,input().split())
    while a|b:
        print(Mondarian(a,b))
        a,b=map(int,input().split())
