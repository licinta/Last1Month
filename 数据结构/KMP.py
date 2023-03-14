class KMP:
    def __init__(self, pattern="aabaaac"):
        self.pattern = pattern
        self.string = None
        self.p = None
        """
        constitude the p-array which will be used in fallback.
        aabaaac   abcabb
        0101220   000120
        """

    def set_string(self, string):
        self.string = string
        self.p = [0]  # the longest match between prefix and suffix
        for i in range(1, len(self.string)):
            j = self.p[i - 1]
            while j and self.string[j] != self.string[i]:
                print(j, i)
                j = self.p[j - 1]
            j += int(self.string[i] == self.string[j])
            self.p.append(j)
        print(self.p)

    def match(self):
        return


kmp = KMP()
kmp.set_string("aabaaa")
kmp = KMP()
kmp.set_string("abcabb")
