from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/merge-two-sorted-lists/
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        cursor = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next

            cursor = cursor.next

        if list1:
            cursor.next = list1
        elif list2:
            cursor.next = list2

        _next = dummy.next
        dummy.next = None
        return _next

