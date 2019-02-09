# https://leetcode.com/problems/toeplitz-matrix/description/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        result = True
        
        for row in range(len(matrix)-1):
            if matrix[row][:-1] != matrix[row+1][1:]:
                result = False
        
        return result
