# https://leetcode.com/problems/number-complement/description/

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        def reverseBin(binary):
            if binary == '0':
                return '1'
            elif binary == '1':
                return '0'
            
        reversedBinary = ''
        
        binary = str(bin(num)[2:])
        for i in binary:
            reversedBinary += reverseBin(i)
        
        return int(reversedBinary, 2)