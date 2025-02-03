class Solution(object):
    def majorityElement(self, nums):
        count={}
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num]=1
        
        result=max(count,key=count.get)
        
        return result
        