# https://leetcode.com/problems/array-partition-i/description/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0    

        for i in range(0, len(nums), 2):
            result += nums[i]
            
        return result