from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0019.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.md
    # 上述連結可參考如何用遞迴實做
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            if fast is not None:
                fast = fast.next

        slow = head
        dummy = ListNode(val=None, next=slow)
        prev = dummy
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # remove target
        prev.next = slow.next
        slow.next = None

        # remove dummy
        _next = dummy.next
        dummy.next = None
        return _next


if __name__ == '__main__':
    head1, _ = create_linklist_from_array([1, 2, 3, 4, 5])
    sol1 = Solution().removeNthFromEnd(head1, 4)
    print(f'{traversal_linklist(sol1)}')
