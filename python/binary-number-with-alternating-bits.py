# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bits = bin(n)
        return all (bits[i] != bits[i + 1] for i in range(len(bits) - 1))