class Solution(object):
    def isAcronym(self, words, s):
        first_letter = [f[0] for f  in words]
        joined_letter="".join(first_letter)
        return joined_letter == s