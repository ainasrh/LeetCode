class Solution(object):
    def lengthOfLastWord(self, s):
        str=s.strip()
        st=str.split(" ")
        res=len(st[-1])
        return res


        