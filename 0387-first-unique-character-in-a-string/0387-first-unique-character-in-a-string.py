from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        seen={}
        for x in s:
            if x not in seen:
                seen[x]=1
            else:
                seen[x]=seen[x]+1
        i=0
        while i<len(s):
            if seen[s[i]]==1:
                return s.index(s[i])
                i=len(str1)
            i+=1
        return -1