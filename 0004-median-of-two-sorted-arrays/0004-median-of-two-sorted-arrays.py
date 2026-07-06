class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        lis = sorted(nums1 + nums2)

        l = len(lis)

        mid = l // 2

        if l % 2 == 0:
            
            
            mid = (lis[mid-1] + lis[mid]) / 2
            print(mid)
            
            return mid
        else:
            return lis[mid]
                
        