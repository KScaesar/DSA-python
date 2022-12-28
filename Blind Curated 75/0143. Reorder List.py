from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/reorder-list/

    # 本題花太久時間
    # 如果是面試中
    # 真的想不到作法, 應該用最簡單的
    # 把 link-list 經過尋訪 變成 array
    # 另用 left, right 來進行解題
    # 面試要求的是速度, 不是學會

    def reorderList(self, head: Optional[ListNode]) -> None:
        # 應該要有能力注意到
        # 題目把 元素分成兩群集

        # O(n)

        if head and head.next is None:
            return

        # 避免後續處理困難, 一定要把 cursor tail 進行為 不重疊
        cursor1, cursor2 = self.splitByMiddle(head)
        cursor2 = self.reverse(cursor2)

        print("cursor1", traversal_linklist(cursor1))
        print("cursor2", traversal_linklist(cursor2))

        prev2 = None
        while cursor1 and cursor2:
            prev2 = cursor2
            next1 = cursor1.next
            next2 = cursor2.next

            cursor1.next = cursor2
            cursor2.next = next1

            cursor1 = next1
            cursor2 = next2

        # 重要步驟 沒執行的話
        # 奇數個元素, 會缺一個元素沒進行串連
        if cursor1 is None and cursor2:
            prev2.next = cursor2

    def splitByMiddle(self, head) -> tuple[ListNode, ListNode]:
        if head and head.next is None:
            return head
        prev = None
        slow = fast = head

        # 注意快慢指針的兩倍速度
        # 是指移動的時候
        # 起點是一樣的, 不要忘記
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 重要步驟
        # 沒執行的話
        # 兩個 list 結尾會重疊
        # [1, 2, 3, 4]:
        # 1. [1, 2, 3]
        # 2. [4, 3]
        prev.next = None
        return head, slow

    def reverse(self, head) -> ListNode:
        if head and head.next is None:
            return head
        ans = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return ans

    def reorderList_timeout(self, head: Optional[ListNode]) -> None:
        # O(n^2)

        # 概念類似 0124. Binary Tree Maximum Path Sum
        # 利用輔助函數遞迴, 藉此求得答案
        if head and head.next is None:
            return

        _next = self.reverse(head.next)
        self.reorderList_timeout(_next)
        head.next = _next


if __name__ == '__main__':
    head1, _ = create_linklist_from_array([1, 2, 3, 4])
    Solution().reorderList_timeout(head1)
    print(traversal_linklist(head1))

    head1, _ = create_linklist_from_array([1, 2, 3, 4, 5])
    Solution().reorderList_timeout(head1)
    print(traversal_linklist(head1))
    print()

    head1, _ = create_linklist_from_array([1, 2, 3, 4])
    Solution().reorderList(head1)
    print(traversal_linklist(head1))

    head1, _ = create_linklist_from_array([1, 2, 3, 4, 5])
    Solution().reorderList(head1)
    print(traversal_linklist(head1))
