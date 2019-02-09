# https://leetcode.com/problems/reshape-the-matrix/description/

import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums