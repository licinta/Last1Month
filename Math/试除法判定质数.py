def prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
    
if __name__=="__main__":
    n=int(input())
    inp=[]
    while len(inp)<n:
        inp.extend(list(map(int ,input().split())))

    for i in inp:
        if prime(i) and i!=1:
            print("Yes")
        else:
            print("No")
        
