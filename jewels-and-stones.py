# https://leetcode.com/problems/jewels-and-stones/description/

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        
        for stone in S:
            if stone in J:
                count += 1
        
        return count
