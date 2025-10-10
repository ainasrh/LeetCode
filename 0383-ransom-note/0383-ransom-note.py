class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        freq = {} 

        for char in magazine:
            freq[char] = freq.get(char,0) + 1
        
        print(freq)

        
        for char in ransomNote:
            if char in freq: 
                freq[char] -= 1
                
                if freq[char] == 0:
                    del freq[char]
            else:
                return False
            
        
        return True
