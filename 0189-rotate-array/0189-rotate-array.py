class Solution(object):
    def rotate(self, nums, k):

        # n = len(nums)
        # k = k % n          
        # for _ in range(k):
        #     popped =  nums.pop()
        #     nums.insert(0,popped)

        
        # return nums
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k] 
        