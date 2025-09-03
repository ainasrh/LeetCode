class Solution(object):
    def isPalindrome(self, s):
        # alpha_ = "".join(char.lower() for char in s if char.isalpha() or char.isdigit())
        # return alpha_ == alpha_[::-1]

        # Two pointers

        l = 0
        r = len(s) - 1
        flag = True

        while l < r:
            if s[l].isalnum() == False:
                l +=1

            elif s[r].isalnum() == False:
                r -=1
                
            else:
                if s[l].lower() == s[r].lower():
                
                    l += 1
                    r -= 1

                else:
                    return False
            
        return True
