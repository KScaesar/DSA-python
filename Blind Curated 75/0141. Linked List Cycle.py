from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/linked-list-cycle/
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    print(Solution())
