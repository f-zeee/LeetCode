class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merge = sorted( nums1 + nums2 )
        n = len(merge) // 2
        res = ( merge[n] + merge[n-1] ) / 2
        if len(merge) % 2:
            res = merge[n]
        return res 


