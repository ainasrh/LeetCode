class Solution(object):
    def singleNumber(self, nums):
        for item in nums:
            if nums.count(item) == 1:
                return item
        