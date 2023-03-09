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
    for i in range(1 << a):
        for column in range(1, b+1):
            for j in range(1 << a):
                temp = i & j
                if temp != 0:  # the brick has a maxium length of 2
                    continue
                temp = i | j
                temp = str(bin(temp))[2:]
                f = False
                for k in range(1, a+1, 2):
                    if k*'0' in temp:
                        f = True
                        break
                if f:  # no odd interval was permitted to appear in all proper state.
                    continue

                dp[column][i] += dp[column-1][j]
    return dp[b][0]


print(Mondarian(2, 4))
