class Solution(object):
    def containsDuplicate(self, nums):
        uni=set(nums)
        print(uni)
        if len(nums) != len(uni):
            return True
        else:
            return False
        
        