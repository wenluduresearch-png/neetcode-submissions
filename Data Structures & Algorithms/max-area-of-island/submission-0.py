class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, self.countArea(grid, i, j))
        return res
        

    def countArea(self, grid: List[List[int]], currX, currY):
        if currX < 0 or currX >= len(grid) or currY < 0 or currY >= len(grid[0]) or grid[currX][currY]==0:
            return 0
        grid[currX][currY] = 0
        d = self.countArea(grid, currX + 1, currY)
        u = self.countArea(grid, currX - 1, currY)
        r = self.countArea(grid, currX, currY + 1)
        l = self.countArea(grid, currX, currY - 1)
        return 1 + d + u + r + l
