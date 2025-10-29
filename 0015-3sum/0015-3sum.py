class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()


        for i in range(len(nums)):
            if i > 0  and nums[i] == nums[i-1]:
                continue;

            j = i + 1
            k = len(nums) - 1

            while j < k:

                ans = nums[i] + nums[j] + nums[k]


                if ans < 0 :
                    j += 1
                elif ans > 0:
                    k -= 1
                elif ans == 0:
                    if [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
                    j += 1
            
        return result




        