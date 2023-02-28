class monostack:
    def __init__(self):
        self.li = []

    def append(self, val):
        while self.li and self.li[-1] >= val:
            self.li.pop()
        self.li.append(val)

    def last(self):
        if self.li == []:
            return None
        return self.li[-1]


n = int(input())
li = list(map(int, input().split()))
mo = monostack()

for i in li:
    mo.append(i)
    if len(mo.li) < 2:
        print(-1, end=' ')
    else:
        print(mo.li[-2], end=' ')
