class Solution(object):
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num)==1:
                unique=num
        return unique        
 
            
            

        