from typing import Optional

from tool import *


class Solution:
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
