# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for i in lists:
            while i:
                res.append(i.val)
                i=i.next
            if i:
                res.append(i.val)

        res=sorted(res, reverse=True)
        nexti=None
        for i in res:
            nexti=ListNode(i,nexti)
        return nexti
    