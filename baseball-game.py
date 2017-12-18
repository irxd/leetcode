# https://leetcode.com/problems/baseball-game/description/

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = []
        
        for op in ops:
            if op == '+':
                result.append(result[-1] + result[-2])
            elif op == 'D':
                result.append(result[-1] * 2)
            elif op == 'C':
                result.pop()
            else:
                result.append(int(op))
                
        return sum(result)