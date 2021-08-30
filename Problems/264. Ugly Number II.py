class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        queue = heapq.heapify(nums)
        temp = [2,3,5]
        
        for i in range(n):
            
            popped = heapq.heappop(nums)
            
            for elem in temp:
                if popped*elem in nums:
                    continue
                heapq.heappush(nums,popped*elem)
            
        return popped