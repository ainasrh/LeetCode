class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_num = len(nums) 
        nums_set = set(nums)  
        result = []

        for i in range(1, max_num + 1):
            if i not in nums_set:  
                result.append(i)
        
        return result
    