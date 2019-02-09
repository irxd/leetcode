# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
