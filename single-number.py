# https://leetcode.com/problems/single-number/description/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        
        for num in nums:
            result ^= num
            print result
            
        return result