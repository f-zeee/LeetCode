# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1==None:
            return l2
        if l2==None:
            return l1
    
        sum=ListNode()
        head=sum
        carry=0
        
        while(True):
            if l1==None and l2==None:
                break
                
            if l1!=None and l2==None:
                sum.val=l1.val+carry
                l1=l1.next
                
            if l1==None and l2!=None:
                sum.val=l2.val+carry
                l2=l2.next
                
            if l1 != None and l2!=None:
                sum.val=l1.val+l2.val+carry
                l1=l1.next
                l2=l2.next
                
            if sum.val>=10:
                    carry=1
                    sum.val=sum.val%10
            else:
                    carry=0
            
            
            cur=sum
            sum.next=ListNode()
            sum=sum.next
             
        cur.next=None   
        if carry==1:
            cur.next=ListNode()
            cur.next.val=1
        return head