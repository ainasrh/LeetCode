class Solution(object):
    def isPerfectSquare(self, num):
        num_root=num**0.5
        print(num_root)
        if num %num_root!=0:
            return False
        else:
            return True
