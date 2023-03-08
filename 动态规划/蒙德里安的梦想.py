def notConflict(bits):
    bits = str(bin(bits))[2:]
    i, j = 0, 0
    while i < len(bits):
        if bits[i] == '1':
            i += 1
        else:
            j = i
            while j<len(bits) and bits[j] == '0':


def f(m, n):
    dp = [[0 for i in range(2 ** m)] for j in range(n)]
    for bits in range(0, 2 ** m):
        if notConflict(bits):
            dp[0][bits] = 1
    for col in range(n):
        for bits in range(0, 2 ** m):
            dp[col][bits] += dp[col - 1][bits]


if __name__ == '__main__':
    a, b = 1, 1
    while a | b != 0:
        a, b = map(int, input().split())
