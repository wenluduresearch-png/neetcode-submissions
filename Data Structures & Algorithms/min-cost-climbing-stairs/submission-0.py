class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [math.inf] * (len(cost) + 2)
        arr[0], arr[1] = 0, 0
        for i in range(len(cost)):
            arr[i + 1] = min(cost[i] + arr[i], arr[i + 1])
            arr[i + 2] = min(cost[i] + arr[i], arr[i + 2])
        print(arr)

        return arr[-2]