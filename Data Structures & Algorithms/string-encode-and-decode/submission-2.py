class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) 
            res += '#' 
            res +=  s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i, j = 0, 0
        res = []
        while i < len(s):
            length = ""
            while s[j] != '#':
                length += s[j]
                j += 1
            res.append(s[j + 1 : j + 1 + int(length)])
            i = j = j + 1 + int(length)

        return res

