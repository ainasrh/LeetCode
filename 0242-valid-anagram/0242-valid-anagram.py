class Solution(object):
    def isAnagram(self, s, t):
        freq = {}
        if len(s) != len(t):
            return False

        for l in s:
            
            freq[l] = freq.get(l,0) + 1

        
        print(freq)
    
        for j in t:
            if j in freq:
                
                if freq[j] >= 1:
                    freq[j]=freq[j] - 1
                else:
                    return False
            else:
                return False
        
        return True

                
    
        print(freq)        

        