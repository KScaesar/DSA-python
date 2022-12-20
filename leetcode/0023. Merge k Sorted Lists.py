from typing import Optional, List

from tool import *


class Solution:
    # https://leetcode.com/problems/merge-k-sorted-lists/
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 還有另一種 利用 heap 的寫法

        n = len(lists)
        if n == 0:  # 不要忘記考慮 n = 0 的情況
            return None
        if n == 1:
            return lists[0]
        # n == 2 的情況, 已經包含在下方
        # if n == 2:
        #     return self.mergeTwoLists(lists[0], lists[1])

        mid = n // 2
        head1 = self.mergeKLists(lists[:mid])
        head2 = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(head1, head2)

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


if __name__ == '__main__':
    obj = Solution()

    l1, _ = create_linklist_from_array([1, 4, 5])
    l2, _ = create_linklist_from_array([1, 3, 4])
    l3, _ = create_linklist_from_array([2, 6])
    sol1 = obj.mergeKLists([l1, l2, l3])
    print(f'expect=[1,1,2,3,4,4,5,6] actual={traversal_linklist(sol1)}\n')
