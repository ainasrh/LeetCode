class Solution(object):
    def strStr(self, haystack, needle):
        try:
            res=haystack.index(needle)
            return res
        except:
            return -1


        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        