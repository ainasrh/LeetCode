class Solution(object):
    def intersection(self, nums1, nums2):

        inter= {}

        for i in range(len(nums1)):
            if nums1[i] in nums2 and nums1[i] not in inter:
                inter[nums1[i]] = i
        
        return inter.keys()

        