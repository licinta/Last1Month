class KMP:
    def __init__(self, pattern="aabaaa"):
        self.pattern = pattern
        self.string = None
        self.p = [0]  # the longest match between prefix and suffix
        for i in range(1, len(self.pattern)):
            j = self.p[i - 1]
            while j and self.pattern[j] != self.pattern[i]:
                print(j, i)
                j = self.p[j - 1]
            j += int(self.pattern[i] == self.pattern[j])
            self.p.append(j)
        """
        constitude the p-array which will be used in fallback.
        aabaaac   abcabb
        0101220   000120
        """

    def set_string(self, string):
        self.string = string

    def match(self):
        i, j = 0, 0
        ans = []
        while i < len(self.string):
            if self.string[i] == self.pattern[j]:
                while i < len(self.string) and j < len(self.pattern) and self.string[i] == self.pattern[j]:
                    i += 1
                    j += 1
                if j == len(self.pattern):
                    ans.append(i - j)
                    j = self.p[j - 1]
                if i == len(self.string):
                    return ans
            else:
                i += 1
        return ans


n = int(input())

kmp = KMP(input())

m = int(input())
kmp.set_string(input())
for i in kmp.match():
    print(i, end=' ')
