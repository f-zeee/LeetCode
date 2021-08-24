#Time Complexity: O(n1+n2)
#Space Complexity: O(n1+n2)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        i1=0
        i2=0
        k=0
        res=[None]*(n1+n2)
        while i1<n1 and i2<n2:
            if nums1[i1]<nums2[i2]:
                res[k]=nums1[i1]
                k+=1
                i1+=1
            else:
                res[k]=nums2[i2]
                k+=1
                i2+=1
        while i1<n1:
            res[k]=nums1[i1]
            k+=1
            i1+=1
        while i2<n2:
            res[k]=nums2[i2]
            k+=1
            i2+=1
        mid=k//2
        return (res[mid]+res[~mid])/2
                
