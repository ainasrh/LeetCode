class Solution(object):
    def checkPerfectNumber(self, num):
        divisor=[n for n in range(1,num) if num%n==0]
        if sum(divisor)==num:
            return True
        else:
            return False
            
        