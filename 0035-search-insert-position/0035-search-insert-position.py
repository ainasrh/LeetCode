class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            i += 1
        return i

