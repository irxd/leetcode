# https://leetcode.com/problems/rotated-digits/description/

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        good_num = 0
        
        for num in range(1, N+1):
            string_num = str(num)
            if '3' in string_num or '7' in string_num or '4' in string_num:
                continue
            if '2' in string_num or '5' in string_num or '6' in string_num or '9' in string_num:
                good_num += 1
        
        return good_num
