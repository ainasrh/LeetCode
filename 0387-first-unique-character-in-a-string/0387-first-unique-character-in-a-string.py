class Solution(object):
    def firstUniqChar(self, s):
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] +=1
            else:
                seen[s[i]] = 1
                
        answer = [k for k,v in seen.items() if v == 1]
        if len(answer) == 0:
            return -1
        else:
            return s.index(answer[0])                    