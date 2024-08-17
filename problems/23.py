# 23. 合并 K 个升序链表
# https://leetcode.cn/problems/merge-k-sorted-lists/
import heapq
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy_head = ListNode()
        dummy = dummy_head
        count = 0

        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, count, head))
                count += 1

        while heap:
            _, _, temp = heapq.heappop(heap)
            if temp.next:
                heapq.heappush(heap, (temp.next.val, count, temp.next))
                count += 1

            dummy.next = temp
            dummy = dummy.next

        return dummy_head.next

    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     setattr(ListNode, "__lt__", lambda a, b: a.val < b.val)
    #     pq = [head for head in lists if head]
    #     heapify(pq)
    #     dummy = cur = ListNode()
    #     while pq:
    #         node = heappop(pq)
    #         if node.next:
    #             heappush(pq, node.next)
    #         cur.next = node
    #         cur = cur.next
    #     return dummy.next
