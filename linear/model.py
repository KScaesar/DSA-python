from dataclasses import dataclass


@dataclass
class ListNode:
    value: int
    previous: 'ListNode' = None
    next: 'ListNode' = None
