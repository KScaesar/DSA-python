from dataclasses import dataclass


@dataclass
class ListNode:
    value: int | None
    previous: 'ListNode' = None
    next: 'ListNode' = None


def traversal_linklist(head: 'ListNode') -> list[int]:
    result = []

    if head == None:
        return result

    cursor: 'ListNode' = head
    while cursor:
        result.append(cursor.value)
        cursor = cursor.next

    return result
