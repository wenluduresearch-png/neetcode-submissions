class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        res = 0
        leftMax = [height[0]] * len(height)

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [height[len(height) - 1]] * len(height)
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        for i in range(len(height)):
            res += min(leftMax[i], rightMax[i]) - height[i]

        return res