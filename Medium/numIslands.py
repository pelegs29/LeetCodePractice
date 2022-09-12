# 200. Number of Islands

class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        lst = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for row, col in lst:
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col] == '1':
                self.dfs(grid, row, col)

    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    islands += 1
        return islands
