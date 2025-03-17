# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        to_str1 = ''
        to_str2 = ''

        # Build the first number string
        curr1 = l1
        while curr1:
            to_str1 = str(curr1.val) + to_str1
            curr1 = curr1.next

        # Build the second number string
        curr2 = l2
        while curr2:
            to_str2 = str(curr2.val) + to_str2
            curr2 = curr2.next

        # Calculate the sum
        result_int = int(to_str1) + int(to_str2)
        result_str = str(result_int)

        # Create the result linked list
        dummy = ListNode(0)
        curr = dummy

        for digit in reversed(result_str):
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next    


        
        
        
            


