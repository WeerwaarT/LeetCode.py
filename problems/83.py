from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        while dummy.next:
            if dummy.val < dummy.next.val:
                dummy = dummy.next
            else:
                dummy.next = dummy.next.next

        return head
