class Solution(object):
    def runningSum(self, nums):
        tsum = 0

        for i in range(len(nums)):
            nums[i] = tsum + nums[i]
            tsum = nums[i]
        
        return nums