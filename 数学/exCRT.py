# exCRT implements

class exCRT:
    def __init__(self, a, m):
        """
        the equations group has a style like :
        x={a1(mod m1), a2(mod m2), ... an(mod mn)}
        this class will find the best answer for that.
        """
        self.crt = list(zip(a, m))

    def exgcd(self, a, b):
        if b == 0:
            return a, 1, 0
        g, s, t = self.exgcd(b, a % b)
        return g, t, s-a//b*t

    def lcm(self, a, b):
        return a*b//self.exgcd(a, b)[0]

    def calc(self):
        import heapq
        heapq.heapify(self.crt)
        while len(self.crt) > 1:
            a1, m1 = heapq.heappop(self.crt)
            a2, m2 = heapq.heappop(self.crt)
            g, s, t = self.exgcd(m1, m2)
            if (a2-a1) % g:
                return -1
            rate = (a2-a1)//g
            s *= rate
            t *= rate
            nea, nem = a1+m1*s, self.lcm(m1, m2)
            heapq.heappush(self.crt, (nea, nem))

        a, m = heapq.heappop(self.crt)
        return a % m
