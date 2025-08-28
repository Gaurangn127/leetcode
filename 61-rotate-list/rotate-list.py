# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head :
            return head
        
        length = 1
        dummy = head

        while dummy.next :
            dummy = dummy.next
            length += 1

        position = k % length  # position: position of new head

        if position == 0 :   #taking(k % length) since rotating the array length times brings it back to its initial state
            return head

        curr = head

        for _ in range(length - position - 1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        dummy.next = head

        return new_head