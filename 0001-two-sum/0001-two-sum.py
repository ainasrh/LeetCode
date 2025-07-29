class Solution(object):
    def twoSum(self, nums, target):
        seen={}

        for num in range(len(nums)):
            value = target - nums[num]
            if value in seen:
                return [seen[value], num]
            else:
                seen[nums[num]]  = num