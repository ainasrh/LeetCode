class Solution(object):
    def isAnagram(self, s, t):
       
        if len(s) != len(t):
            return False

        # Take unique characters from s
        char = set(s)

        # iterate through that uniue characters
        for c in char:
            #  Check two Character count are same then if not it not a anagram word
            if s.count(c) != t.count(c):
                return False
        return True
