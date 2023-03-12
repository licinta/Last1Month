def nqueue(n):
    li = [i for i in range(1, n + 1)]

    def check(i):
        for j in range(len(i) - 1):
            for k in range(1, len(i) - j):
                if abs(i[j + k] - i[j]) == k:
                    return False
        return True

    def fprint(i):
        for j in i:
            temp = ['.' for k in range(len(li))]
            temp[j - 1] = 'Q'
            print(''.join(temp))


    from itertools import permutations
    for i in permutations(li):
        if check(i):
            fprint(i)
            print()
nqueue(int(input()))