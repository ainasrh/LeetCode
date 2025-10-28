class Solution(object):
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):
            bal = target - nums[i]
                
            if bal in seen:
                return [seen[bal],i]
        
            if nums[i] not in seen:
                seen[nums[i]] = i
                

                
        print(seen)