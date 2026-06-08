from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: # Added defensive check for empty grid
            return 0
            
        rows = len(grid)
        cols = len(grid[0]) # ✅ FIX: Use grid[0] for column count
        island_count = 0
        
        def sink_island(g, r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or g[r][c] == "0":
                return
            g[r][c] = "0" 
            sink_island(g, r + 1, c)
            sink_island(g, r - 1, c)
            sink_island(g, r, c + 1)
            sink_island(g, r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    sink_island(grid, r, c)
                    
        return island_count # ✅ This will now execute and safely return an integer
