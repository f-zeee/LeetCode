class Solution:
    def twoSum(self, nums, target):        
        for i, n in enumerate(nums):
            for j in range (i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return i,j
        