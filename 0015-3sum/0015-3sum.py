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
                    result.append([nums[i],nums[j],nums[k]])
                    
                    while j < k and nums[j] == nums[j+1]:
                        j +=1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
             
        return result




        