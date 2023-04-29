# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        prev=None
        r=1
        while r<=left:
            prev=curr
            curr=curr.next
            r+=1
        leng=right-left
        l=left
        while l <=leng and curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            l+=1
        return prev
            
