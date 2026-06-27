class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: return stones[0]
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)
        return 0 if not stones else -heapq.heappop(stones)