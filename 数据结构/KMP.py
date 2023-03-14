class KMP:
    def __init__(self, pattern="aabaaa"):
        """
            constitude the p-array which will be used in fallback.
            aabaaac   abcabb
            0101220   000120
        """
        self.pattern = pattern
        self.string = None
        self.p = [0]  # the longest match between prefix and suffix
        for i in range(1, len(self.pattern)):
            j = self.p[i - 1]
            while j and self.pattern[j] != self.pattern[i]:
                j = self.p[j - 1]
            j += int(self.pattern[i] == self.pattern[j])
            self.p.append(j)
        # print(self.p)

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
                    # if f:
                    #     print(i, j, self.string[i], self.pattern[j])

                if j == len(self.pattern):
                    """successfully"""
                    ans.append(i - j)
                    i -= self.p[j - 1]
                    j = 0
                    continue
                if i == len(self.string):
                    """run out"""
                    return ans
                """failed"""
                i -= self.p[j - 1]
                j = 0

            else:
                i += 1
        return ans


n = int(input())
kmp = KMP(input())
m = int(input())
kmp.set_string(input())
for i in kmp.match():
    print(i, end=' ')
