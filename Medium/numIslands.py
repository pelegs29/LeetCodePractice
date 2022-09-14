# 200. Number of Islands

class Solution:
    def dfs(self, grid, r, c, max_row, max_col):
        grid[r][c] = '0'
        lst = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for row, col in lst:
            if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col] == '1':
                self.dfs(grid, row, col, max_row, max_col)

    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c, rows, cols)
                    islands += 1
        return islands
