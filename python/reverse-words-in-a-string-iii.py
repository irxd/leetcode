# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        splitted =  s.split( )
        result = []
        
        for word in splitted:
            result.append(word[::-1])
        
        return (' ').join(result)
        