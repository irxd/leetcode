# https://leetcode.com/problems/next-greater-element-i/description/

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        cache = {}
        stack = []
        result = []
        
        for num in nums:
            while len(stack) and stack[-1] < num:
                cache[stack.pop()] = num
            stack.append(num)

        for num in findNums:
            result.append(cache.get(num, -1))
            
        return result