class Solution(object):
    def containsDuplicate(self, nums):
        maping = {}

        for num in nums:
            if num in maping:
                return True
            
            maping[num] = 1
        return False