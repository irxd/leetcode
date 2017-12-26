# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        # 1 0 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1 
