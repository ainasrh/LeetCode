class Solution(object):
    def differenceOfSum(self, nums):
        num_sum=sum(nums)
        digit_sum=0

        join_nums="".join(map(str,nums))
        for num in join_nums:
            digit_sum+=int(num)

        result=num_sum-digit_sum
        return result
        