# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        l = 1           #length

        while curr.next :
            curr = curr.next
            l += 1
        
        if (l == 1 and n == 1) or l == n :
            return head.next
        
        prev = head
        for _ in range(l - n -1):
            prev = prev.next
        
        prev.next = prev.next.next

        return head

