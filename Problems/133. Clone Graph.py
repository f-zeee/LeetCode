"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#return copy.deepcopy(node)

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        seen={}
        
        def dfs(node,seen):
            newNode=Node(node.val)
            #newNode.val=node.val
            seen[newNode.val]=newNode #index of the nodes is same as the node's val
            newNeighbors=[]
            for n in node.neighbors: #we have to traverse through the known node because we don't know the neighbors of newNode
                if n.val not in seen:
                    newNeighbors.append(dfs(n,seen))
                else:
                    newNeighbors.append(seen[n.val])
                    
            newNode.neighbors=newNeighbors
            return newNode
        return dfs(node,seen)
            