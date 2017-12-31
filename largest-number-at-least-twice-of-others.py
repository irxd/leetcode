# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        
        for num in nums:
            if num != max_num and max_num < num * 2:
                return -1
            
        return nums.index(max_num)
