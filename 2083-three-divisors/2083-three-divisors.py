class Solution(object):
    def isThree(self, n):
        count=0
        for num in range(1,n+1):
            
            if n%num==0:
                count+=1
        if count ==3:
            return True        
        else:
            return False      
        