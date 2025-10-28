class Solution(object):
    def reverseWords(self, s):
        
        splited = s.split()
        
        result = " ".join(splited[::-1]).strip()

        return result 