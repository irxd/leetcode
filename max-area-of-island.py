# https://leetcode.com/problems/max-area-of-island/description/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowNum, colNum = len(grid), len(grid[0])

        def dfs(row, col):
            if 0 <= row < rowNum and 0 <= col < colNum and grid[row][col]:
                grid[row][col] = 0
                return 1 + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1)
            return 0

        areas = [dfs(row, col) for row in range(rowNum) for col in range(colNum) if grid[row][col]]
        print areas
        return max(areas) if areas else 0
