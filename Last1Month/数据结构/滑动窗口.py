import collections

class maxslide:
    def __init__(self,length):
        self.li=collections.deque()
        self.maxsize=length

    def append(self,idx,val):
        while self.li and self.li[-1][1]<val:
            self.li.pop()

        self.li.append((idx,val))

        while self.li and self.li[-1][0]-self.li[0][0]>=self.maxsize:
            self.li.popleft()

    def Max(self):
        return self.li[0][1]

    def __str__(self):
        return [i[1] for i in self.li]


class minslide:
    def __init__(self,length):
        self.li=collections.deque()
        self.maxsize=length

    def append(self,idx,val):
        while self.li and self.li[-1][1]>val:
            self.li.pop()

        self.li.append((idx,val))

        while self.li and self.li[-1][0]-self.li[0][0]>=self.maxsize:
            self.li.popleft()

    def Min(self):
        return self.li[0][1]

    def __str__(self):
        return [i[1] for i in self.li]


n,m=map(int,input().split())
li=list(map(int,input().split()))
s2=maxslide(m)
s1=minslide(m)
mn,mx=[],[]
for idx,i in enumerate(li):
    s1.append(idx,i)
    s2.append(idx,i)
    if idx>=m-1:
        mn.append(s1.Min())
        mx.append(s2.Max())

print(*mn)
print(*mx)
