class Solution(object):
    def findTheDifference(self, s, t):
        
        freq = {}

        for char in s:
            freq[char] = freq.get(char,0) + 1
        
        

        
        for tchar in t:

            if tchar in freq:
                freq[tchar] -= 1 
                
                if freq[tchar] == 0:
                    del freq[tchar]

                
                

            else:
                return tchar
        