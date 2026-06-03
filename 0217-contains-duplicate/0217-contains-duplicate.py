class Solution(object):
    def containsDuplicate(self, nums):
        
        mapping =  {}

        for i in range(len(nums)):
            if nums[i] in mapping:
                return True
            
            mapping[nums[i]] = i

        
        return False