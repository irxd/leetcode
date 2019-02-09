# https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major_num, count = nums[0], 0
        
        for index, num in enumerate(nums):
            if count == 0:
                count += 1
                major_num = nums[index]
            elif major_num == nums[index]:
                count += 1
            else:
                count -= 1
                
        return major_num
