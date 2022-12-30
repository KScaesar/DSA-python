from typing import Optional

from tool import *


class Solution:
    # https://leetcode.com/problems/reverse-linked-list/
    # https://leetcode.com/problems/reverse-linked-list/solutions/58127/python-iterative-and-recursive-solution/?orderBy=most_votes
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cursor = head
        while cursor:
            _next = cursor.next
            cursor.next = prev
            prev = cursor
            cursor = _next
        return prev


if __name__ == '__main__':
    print(Solution())
