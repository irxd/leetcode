# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isDivisable(num):
            num_string = str(num)
            divisable = True
            
            for n in num_string:
                if (int(n) == 0) or (num % int(n) != 0) :
                    divisable = False
                    break
                    
            return divisable
        
        result = []
        
        for num in range(left, right+1):
            if isDivisable(num):
                result.append(num)
        
        return result