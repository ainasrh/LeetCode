from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        for char in s:
            freq[char] = freq.get(char,0) + 1 


        for ind,value in enumerate(s):
            if freq[value] == 1:
                return ind
        
        
        return -1

