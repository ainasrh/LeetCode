class Solution(object):
    def findTheDifference(self, s, t):
        # for i in t:
        #     if not i in s:
        #         return i
        
        s_sum = sum(ord(ch) for ch in s)
        t_sum = sum(ord(ch) for ch in t)
        return chr(t_sum-s_sum)