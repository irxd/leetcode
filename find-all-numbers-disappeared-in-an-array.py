# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))
