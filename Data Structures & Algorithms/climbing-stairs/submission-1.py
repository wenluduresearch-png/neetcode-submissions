class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,2]
        if n < 3: return n
        for i in range(2, n):
            tmp = arr[0] + arr[1]
            arr[0] = arr[1]
            arr[1] = tmp
        return arr[1]