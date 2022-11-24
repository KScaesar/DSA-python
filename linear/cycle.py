import factory
from model import ListNode, traversal_linklist


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


if __name__ == '__main__':
    link1 = factory.cycle_linklist(False)
    cross_node, has = has_cycle(link1)
    print(f'link1 has cycle? {has}')
    if not has:
        traversal_linklist(link1)

    link2 = factory.cycle_linklist(True)
    cross_node, has = has_cycle(link2)
    print(f'\nlink2 has cycle? {has}')
    if not has:
        traversal_linklist(link2)
    else:
        print(f'cross node data: {cross_node}')
