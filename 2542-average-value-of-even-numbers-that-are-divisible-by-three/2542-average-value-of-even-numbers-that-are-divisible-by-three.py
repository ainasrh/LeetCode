class Solution(object):
    def averageValue(self, nums):
        total=[]
        for num in nums:
            if num%2==0 and num%3==0:
                total.append(num)
        if not total:
            return 0        
        return sum(total)//len(total)      
