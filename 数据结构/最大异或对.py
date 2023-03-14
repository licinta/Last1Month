from array import array


class Trie:
    def __init__(self, N):
        self.ptr = 0
        # self.word = [[0 for i in range(2)] for j in range(N)]
        self.word = [array('l', [0, 0]) for i in range(N)]
        self.cnt = [0 for i in range(N)]

    def insert(self, word):
        p = 0
        for i in word:
            oi = int(i)
            if not self.word[p][oi]:
                self.ptr += 1
                self.word[p][oi] = self.ptr
            p = self.word[p][oi]

        self.cnt[p] += 1

    def query(self, word):
        p = 0
        ans = 0
        for i in word:
            oi = int(i)
            if self.word[p][oi ^ 1] == 0:
                ans <<= 1
                ans += 0
                p = self.word[p][oi]
            else:
                ans <<= 1
                ans += 1
                p = self.word[p][oi ^ 1]
        return ans


BIT = 31
n = int(input())
li = list(map(int, input().split()))
li = list(map(lambda i: str(bin(i))[2:].rjust(BIT, '0'), li))

trie = Trie(BIT * (n + 5))
for i in li:
    trie.insert(i)

ans = 0
for i in li:
    ans = max(trie.query(i), ans)
print(ans)
