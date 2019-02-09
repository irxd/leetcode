# https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ['Q', 'W', 'E', 'R', 'T', 'T', 'Y', 'U', 'I', 'O', 'P']
        row2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        row3 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        
        def iterateChar(word,row):
            for char in word:
                if char.upper() not in row:
                    return False
            return True
        
        def inputCheck(word):   
            if word[0].upper() in row1:
                return iterateChar(word, row1)
            elif word[0].upper() in row2:
                return iterateChar(word, row2)
            elif word[0].upper() in row3:
                return iterateChar(word, row3)   
        
        result = []
        
        for word in words:
            if inputCheck(word):
                result.append(word)
        
        return result