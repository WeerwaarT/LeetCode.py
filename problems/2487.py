from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Can be solved using recursion, but I don't want to. ^^
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        queue = [head]
        while head.next:
            if head.next.val > head.val:
                while queue:
                    if queue[-1].val < head.next.val:
                        queue.pop()
                    else:
                        break

            queue.append(head.next)
            head = head.next

        dummy_head = ListNode()
        head = dummy_head
        for node in queue:
            head.next = node
            head = head.next

        return dummy_head.next


if __name__ == '__main__':
    print(Solution().removeNodes(ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8)))))))
