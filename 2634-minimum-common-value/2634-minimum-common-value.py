class Solution(object):
    def getCommon(self, nums1, nums2):
        set2 = set(nums2)
        for num in nums1:
            if num in set2:
                return num
        return -1        

        