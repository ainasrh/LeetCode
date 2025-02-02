class Solution(object):
    def missingNumber(self, nums):
        nums_length=len(nums)
        if 0 not in nums:
            return 0
        for i in range(0,nums_length):
            if nums[i]==0:
                for j in range(1,nums_length+1):
                    if j not in nums:
                        nums[i]=j
                        return j
            