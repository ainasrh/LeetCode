class Solution(object):
    def decompressRLElist(self, nums):
        result=[]
        for i in range(len(nums) // 2):
            freq=nums[2*i]
            value=nums[2*i+1]
            result +=[value] * freq

        return result
                