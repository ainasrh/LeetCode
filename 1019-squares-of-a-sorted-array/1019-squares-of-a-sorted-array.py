class Solution(object):
    def sortedSquares(self, nums):
        # return sorted([x*x for x in nums])
        l = 0
        r = len(nums) - 1
        result = []

        while (l <= r):
            if abs(nums[l]) > abs(nums[r]):
                result.append(nums[l] ** 2)
                l += 1
            else:
                result.append(nums[r] ** 2)
                r -= 1
        
        result.reverse()
        return result
        