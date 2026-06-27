class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Python的heapq默认按列表的第一个元素排序，如果第一个元素相同，则比较第二个，以此类推。
        minHeap = []
        for x, y in points:
            minHeap.append([(x**2 + y**2), x, y])
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res