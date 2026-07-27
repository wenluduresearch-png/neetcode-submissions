from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # 收集所有初始腐烂橘子，并统计新鲜橘子数
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))   # (行, 列, 分钟)
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            r, c, t = queue.popleft()
            minutes = max(minutes, t)   # 记录最大时间
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2      # 标记为腐烂
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
        
        return minutes if fresh == 0 else -1