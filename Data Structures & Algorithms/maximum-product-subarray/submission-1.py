class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        min_sub, max_sub = 1, 1
        for n in nums:
            # if n == 0:
            #     min_sub, max_sub = 1, 1
            #     continue
            tmp = max_sub * n
            max_sub = max(tmp, min_sub * n, n)
            min_sub = min(tmp, min_sub * n, n)
            res = max(res, max_sub)
        return res