def Comb(a, b):
    ans = 1
    for i in range(b+1, a+1):
        ans *= i
    for i in range(1, a-b+1):
        ans //= i
    return ans


a, b = map(int, input().split())
print(Comb(a, b))
