class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        res = []
        while i < len(s):
            count = ""
            while s[j] != '#':
                count += s[j]
                j += 1
            res.append(s[j +1: j + int(count) +1])
            i = j = j + int(count) +1
        return res
