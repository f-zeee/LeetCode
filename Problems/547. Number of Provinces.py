class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UnionFind(object):
            def __init__(self, n): #we have to initialize this with given number of elements
                self.parents = list(range(n)) #for each element, we will annotate its boss that will be size of n here
                self.sizes = [1] * n #when we have 2 similar boss, we have to merge the smaller company into the bigger one, so that's why we have the boss

            def _find_iterative(self, i):
                # 1 path to find the root/actual boss
                root = i
                while self.parents[root] != root:
                    root = self.parents[root]
                # 2 updatig every node in the path to let then know who is the actual boss/root
                while self.parents[i] != root:
                    parent = self.parents[i]
                    self.parents[i] = root
                    i = parent
                return root

            find = _find_iterative

            def union(self, p, q):
                root_p, root_q = map(self.find, (p, q))
                if root_p == root_q: 
                    return
                small, big = sorted([root_p, root_q], key=lambda x: self.sizes[x])
                self.parents[small] = big
                self.sizes[big] += self.sizes[small]    
        
        n=len(isConnected)
        uf=UnionFind(n)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i,j)
                    
        prov=set()
        for i in range(n):
            prov.add(uf.find(i))
            
        return len(prov)