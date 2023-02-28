# 扩展中国剩余定理

class exCRT:
    def __init__(self, lia=[], lim=[]):
        self.crt = list(zip(lia, lim))

    def exgcd(self, a, b):
        if b == 0:
            return a, 1, 0
        g, s, t = self.exgcd(b, a % b)
        return g, t, s-a//b*t

    def lcm(self, a, b): return a*b//self.exgcd(a, b)[0]

    def calculate(self):
        """
            return -1 means the equation group is unvalid.
        """
        import heapq
        heapq.heapify(self.crt)
        while len(self.crt) > 1:
            a1, m1 = heapq.heappop(self.crt)
            a2, m2 = heapq.heappop(self.crt)
            gcd, s, t = self.exgcd(m1, m2)
            if (a2-a1) % gcd != 0:
                return -1

            rate = (a2-a1)//gcd
            # increase by rate
            s *= rate
            t *= rate

            nea, nem = a1+s*m1, self.lcm(m1, m2)
            heapq.heappush(self.crt, (nea, nem))
        lasta, lastm = heapq.heappop(self.crt)
        return lasta % lastm


n = int(input())
a, m = [], []
for i in range(n):
    x, y = map(int, input().split())
    a.append(y)
    m.append(x)
crt = exCRT(a, m)
print(crt.calculate())
