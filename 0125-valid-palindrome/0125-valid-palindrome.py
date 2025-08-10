class Solution(object):
    def isPalindrome(self, s):
        alpha_ = "".join(char.lower() for char in s if char.isalpha() or char.isdigit())
        return alpha_ == alpha_[::-1]