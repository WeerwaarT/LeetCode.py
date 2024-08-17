# 21. 合并两个有序链表
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        temp = dummy_head

        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        temp.next = list1 if list1 else list2

        return dummy_head.next

    # 下面这个写法比较没必要
    def mergeTwoLists_1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists_1(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_1(list1, list2.next)
            return list2

    # 所有提交里最快的写法，第一个if里or的应用我确实没想到
    def mergeTwoLists_3(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # edge case
        if not l1 or not l2:
            return l1 or l2

        # create a dummy node
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val > l2.val:
                # swap l1 and l2, the whole list start from the current node
                l1, l2 = l2, l1
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        cur.next = l1 or l2

        return dummy.next