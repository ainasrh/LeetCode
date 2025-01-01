class Solution(object):
    def countDigits(self, num):
        n=str(num)
        count=0
        for i in range(len(n)):
            if num%int(n[i])==0:
                count+=1
        return count        

