# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        consecutive = 0
        result = 0
        
        for num in nums:
            if num == 1:
                consecutive += 1
                result = max(result, consecutive)
            else:
                consecutive = 0
        
        return result