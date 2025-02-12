class Solution(object):
    def smallestEvenMultiple(self, n):
        if n%2 == 0:
            return n
        else:
            result=n*2
            if result % 2 == 0 :
                return result
        