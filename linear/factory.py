from model import ListNode


def linklist_from_array(nums: list[int]) -> ListNode | None:
    dummy = ListNode(None)

    if nums is None:
        return None

    cursor = dummy
    for v in nums:
        cursor.next = ListNode(v)
        cursor = cursor.next

    _next = dummy.next
    dummy.next = None
    return _next


def cycle_linklist(has_circle: bool) -> 'ListNode':
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
