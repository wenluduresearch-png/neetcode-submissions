class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in n_set:
                length = 0
                while n + length in n_set:
                    length += 1
                longest = max(longest, length)
        return longest
