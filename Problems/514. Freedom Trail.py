from collections import defaultdict
class Solution:
    
    def findRotateSteps(self, ring: str, key: str) -> int:
        mapping=defaultdict(list) #enumerate operates on a list so we are converting mapping to a list
        n,m=len(ring),len(key)
        for i, j in enumerate(ring):
            mapping[j] += i, #we are mapping letters to characters of the ring
            
        def minDist(i,j):
            return min(abs(i-j), n-abs(i-j))
        
        @lru_cache(None)
        def solve(ptr,index):#ptr is pointer for ring and index is pointer for key
            if index>=m:
                return 0
            steps=1
            if ring[ptr]==key[index]:
                steps+=solve(ptr,index+1)
            else:
                char = mapping[key[index]]
                insertele=bisect.bisect_right(char, ptr)#if ptr is already present in char the insertion point will be right of any existing entries
                left,right=insertele-1, insertele%len(char)
                #left & right indicate anti-clockwise & clockwise directions in the ring from the respective element
                steps+=min(minDist(ptr,char[left])+solve(char[left],index+1),minDist(ptr,char[right])+solve(char[right],index+1))
            return steps
        return solve(0,0)

                
        