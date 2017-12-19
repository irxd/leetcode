# https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def adjacentCheck(row, col):
            adjacent = (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)  
            perimeter = 0
            for row, col in adjacent:
                if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 0:
                    perimeter += 1
            return perimeter
            
        result = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    result += adjacentCheck(row, col)
        
        return result