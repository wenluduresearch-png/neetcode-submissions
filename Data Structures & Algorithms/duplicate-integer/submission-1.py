class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return True
            hash_map[nums[i]] = 1
        return False