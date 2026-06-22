class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            hashSet = set()
            longest = 0
            j = i
            while j < len(s) and s[j] not in hashSet:
                longest += 1
                hashSet.add(s[j])
                j += 1
            res = max(longest, res)
        return res
