class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = counter.most_common()
        res = []
        for i in range(k):
            res.append(sorted_counter[i][0])
        return res
