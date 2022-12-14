from tool import ListNode, traversal_linklist


def has_cycle(head: ListNode) -> tuple[ListNode | None, bool]:
    if head == None:
        return None, False

    fast: 'ListNode'
    slow: 'ListNode'
    fast = slow = head

    # 記住這個條件
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if fast is slow:
            break

    if fast == None:
        return None, False

    # 回到起點
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow, True


def create_cycle_linklist(has_circle: bool) -> 'ListNode':
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


if __name__ == '__main__':
    link1 = create_cycle_linklist(False)
    cross_node, has = has_cycle(link1)
    print(f'link1 has cycle? {has}')
    if not has:
        traversal_linklist(link1)

    link2 = create_cycle_linklist(True)
    cross_node, has = has_cycle(link2)
    print(f'\nlink2 has cycle? {has}')
    if not has:
        traversal_linklist(link2)
    else:
        print(f'cross node data: {cross_node}')
