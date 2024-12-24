class Solution(object):
    def removeElement(self, nums, val):
        c=0
        for i in nums:
            if i!=val:
                nums[c]=i
                c=c+1


        return c         

        

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        