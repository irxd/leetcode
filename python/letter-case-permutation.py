# https://leetcode.com/problems/letter-case-permutation/description/

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = ['']
        for char in S:
            if char.isalpha():
                result = [i+j for i in result for j in [char.lower(), char.upper()]]
            else:
                result = [i+char for i in result]
            print result
        return result
