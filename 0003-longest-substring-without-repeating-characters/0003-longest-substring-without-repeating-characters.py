class Solution(object):
    def lengthOfLongestSubstring(self, s):
            max_len = 0

            seen = []

            left = 0


            for right in range(left,len(s)):
                
                while s[right] in seen:
                        seen.remove(s[left])
                        
                        left += 1
                    
                
                seen.append(s[right])
                
                if max_len < len(seen):
                    max_len = len(seen)
                    
            return max_len
                
                            

