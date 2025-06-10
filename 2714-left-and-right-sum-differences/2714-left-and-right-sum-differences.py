class Solution(object):
    def leftRightDifference(self, nums):
        num_sum_left=0
        num_sum_right = 0
        n = len(nums)
        left_sum= [0] * n
        right_sum=[0] * n


        for i in range(n):
            if i != 0:
                # LEFT sum
                num_sum_left += nums[i-1]
                left_sum[i]= num_sum_left
                # Right sum
                num_sum_right += nums[(n-i)]
                
                right_sum[(n-i)-1] = num_sum_right
            

        result=[abs(left_sum[i] - right_sum[i]) for i in range(len(nums))]


        return result    

        