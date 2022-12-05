import heapq
from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/merge-k-sorted-lists/description/
    # N 是所有的 node 個數，K 是所有 list 個數
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        return self.mergeKLists_heap(lists)
        # return self.mergeKLists_divide_conquer(lists)

    def mergeKLists_heap(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        # O(N*logK)
        # https://afteracademy.com/blog/merge-k-sorted-lists/

        min_heap = []
        for i, head in enumerate(lists):
            # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
            # heapq.heappush(min_heap, (head.val, head))
            # 既然 ListNode 無法比較, 就用 index 類比為 指針
            # 或者也可以自己另外實現
            # ListNode.__eq__ = lambda self, other: self.val == other.val
            # ListNode.__lt__ = lambda self, other: self.val < other.val
            # https://leetcode.com/problems/merge-k-sorted-lists/solutions/465094/problems-with-python3-and-multiple-solutions/
            if head:
                heapq.heappush(min_heap, (head.val, i))

        dummy = ListNode(None)
        cursor = dummy

        while len(min_heap):
            _, index = heapq.heappop(min_heap)
            node = lists[index]

            cursor.next = node
            cursor = cursor.next
            _next = node.next
            if _next:
                lists[index] = _next
                heapq.heappush(min_heap, (_next.val, index))

        _next = dummy.next
        dummy.next = None
        return _next

    # @debug_helper
    def mergeKLists_divide_conquer(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        # n == 2 的 情況, 其實下方邏輯已經有包含
        #
        # elif n == 2:
        #     head1 = lists[0]
        #     head2 = lists[1]
        #     return self.merge(head1, head2)

        mid = n // 2
        head1 = self.mergeKLists_divide_conquer(lists[:mid])
        head2 = self.mergeKLists_divide_conquer(lists[mid:])
        return self.merge(head1, head2)

    def merge(self, head1, head2) -> Optional[ListNode]:
        # merge 寫法要再確定, 有點忘記了
        # linklist 和 array 都要複習一下

        if head1 is None or head2 is None:
            return head1 if head1 is not None else head2
        # if head1 is None or head2 is None:
        #     return head1 if head1 is not None else head2
        # elif head1 is None and head2 is None:
        #     return None

        dummy = ListNode(None)
        cursor = dummy

        while head1 is not None and head2 is not None:
            if head1.val > head2.val:
                cursor.next = head2
                head2 = head2.next
            else:
                cursor.next = head1
                head1 = head1.next
            cursor = cursor.next

        cursor.next = head2 if head2 is not None else head1
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

    # print(traversal_linklist(obj.merge(l1, l2)))
