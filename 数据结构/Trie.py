class Trie:
    def __init__(self, N):
        """
        self.word: contains N nodes, which implements all possible endings (char = 256)
        self.ptr: current last node
        self.cnt: the word's number
        =abcdefghijklmnopqrstuvwxyz
        0++1++++++++++++4++++++++++
        1+++2++++++++++6+++++++++++
        2++++3+++++++++++++++++++++
        3++++++++++++++++++++++++++
        4++++++++5+++++++++++++++++
        5++++++++++++++++++++++++++
        6++++++++++++++++++7+++++++
        7++++++++++++++++++++++++++
        8++++++++++++++++++++++++++
        9++++++++++++++++++++++++++
        A++++++++++++++++++++++++++
        B++++++++++++++++++++++++++
        ===========================
        word1:cde
        word2:pi
        word3:cos

        Test:
        trie = Trie(100)
        trie.insert("hello")
        trie.insert("he")
        trie.insert("hope")
        print(trie.query("h"))
        print(trie.query("he"))
        print(trie.query("hope"))
        """
        self.word = [[0 for i in range(128)] for j in range(N)]
        self.cnt = [0 for i in range(N)]
        self.ptr = 0

    def insert(self, word):
        p = 0
        for i in word:
            oi = ord(i)
            if self.word[p][oi] == 0:
                self.ptr += 1
                self.word[p][oi] = self.ptr
            p = self.word[p][oi]
        self.cnt[p] += 1

    def query(self, word):
        p = 0
        for i in word:
            oi = ord(i)
            p = self.word[p][oi]
            if p == 0:
                return 0
        return self.cnt[p]


n = int(input())
trie = Trie(100005)
for i in range(n):
    # print("*" * 21)
    # print(trie.ptr)
    # for k in trie.word[:10]:
    #     print(k[97:100])
    op, word = input().split()
    if op == "I":
        trie.insert(word)
    else:
        print(trie.query(word))
