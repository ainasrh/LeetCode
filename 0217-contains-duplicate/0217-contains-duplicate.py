class Solution(object):
    def containsDuplicate(self, nums):
        count_dict = {}
        for i in nums:
            if i in count_dict:
                return True
            else:
                count_dict[i] = 1
                continue; 
        return False     

