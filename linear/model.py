from dataclasses import dataclass


@dataclass
class ListNode:
    value: int
    previous: 'ListNode' = None
    next: 'ListNode' = None


def create_example_linklist(has_circle: bool) -> 'ListNode':
    # False:
    # 0->1->2->3->4->5->None
    #
    # True:
    # 0->1->2->3->4
    #           \  \
    #            <-5

    n4 = ListNode(4)
    n3 = ListNode(3, next=n4)
    n2 = ListNode(2, next=n3)
    n1 = ListNode(1, next=n2)
    n0 = ListNode(0, next=n1)

    if has_circle:
        n5 = ListNode(5, next=n3)
    else:
        n5 = ListNode(5)
    n4.next = n5

    return n0


def traversal_linklist(head: 'ListNode') -> list[int]:
    result = []

    if head == None:
        return result

    cursor: 'ListNode' = head
    while cursor:
        result.append(cursor.value)
        cursor = cursor.next

    return result
