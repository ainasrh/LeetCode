class Solution(object):
    def isAnagram(self, s, t):
       
        if len(s) != len(t):
            return False

    
        # char = set(s)


        # for c in char:
        
        #     if s.count(c) != t.count(c):
        #         return False
        # return True
        
        freq = {}

        for char in s:

            freq[char] = freq.get(char,0) + 1
        
        for char in t:
            if char not in freq:
                return False
            else:
                freq[char] -=1
                if freq[char] == 0:
                    del freq[char]

        
        return True