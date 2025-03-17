# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if not head: # Check for empty list
            return head

        while current and current.next: # Check if current and current.next are not None
            if current.val == current.next.val: # Access val, not value
                current.next = current.next.next
            else:
                current = current.next
        return head