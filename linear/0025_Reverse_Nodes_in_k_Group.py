from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/reverse-nodes-in-k-group/
    # https://labuladong.github.io/algo/2/19/20/

    def reverseKGroup_v2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        cnt = k
        cursor = head
        prev = None
        while cnt and cursor:
            cnt -= 1
            prev = cursor
            cursor = cursor.next
        if prev:
            prev.next = None

        sub = self.reverseKGroup_v2(cursor, k)

        # 不滿足 k 數量的 不需要 反轉
        if cnt > 0:
            prev.next = sub
            return head

        cursor = head
        prev = None
        while cursor:
            _next = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = _next
        head.next = sub
        return prev

    # @debug_helper
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cursor1 = head
        for _ in range(k):
            if cursor1 is None:
                return head
            else:
                cursor1 = cursor1.next

        prev = None
        cursor2 = head

        # 下方可單獨抽出一個 reverse 函數
        # 反转区间 [cursor2, cursor1) 的元素，注意是左闭右开
        # 面對 k 個距離的題目, 分別兩個游標
        # 比較好處理
        # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        #
        # 另一種判斷條件
        # for _ in range(k):
        while cursor2 is not cursor1:
            _next = cursor2.next
            cursor2.next = prev
            prev = cursor2
            cursor2 = _next

        sub_head = self.reverseKGroup(cursor2, k)
        head.next = sub_head
        return prev


if __name__ == '__main__':
    obj = Solution()

    # head1, _ = create_linklist_from_array([1, 2, 3, 4, 5])
    # sol1 = obj.reverseKGroup(head1, 3)
    # print(f'{traversal_linklist(sol1)}')

    head1, _ = create_linklist_from_array([1, 2, 3, 4, 5])
    sol1 = obj.reverseKGroup_v2(head1, 3)
    print(f'{traversal_linklist(sol1)}')
