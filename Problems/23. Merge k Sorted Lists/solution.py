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
        #we are sorting this is reverse order beacuse we have to return a linked list and my loop for creating a linked list traverses from the beginning
        nexti=None
        for i in res:
            nexti=ListNode(i,nexti)
        return nexti
    