class Solution(object):
    def missingNumber(self, nums):

        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        
        n = len(nums)

        sum_nums = (n) * (n+1) // 2

        curr = sum(nums)
        return  sum_nums - curr
        
    