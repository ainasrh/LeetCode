class Solution(object):
    def findTheDifference(self, s, t):
        # for i in t:
        #     if not i in s:
        #         return i
        
        count_s = Counter(s)
        count_t=Counter(t)
        return list(count_t - count_s)[0]