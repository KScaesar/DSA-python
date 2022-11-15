from model import ListNode, create_example_linklist, traversal_linklist


def reverse_list_iterative(head: 'ListNode') -> 'ListNode':
    if head == None:
        return None

    next: 'ListNode' = None
    cursor: 'ListNode' = head
    prev: 'ListNode' = None

    while cursor:
        next = cursor.next
        cursor.next = prev
        prev = cursor
        cursor = next

    return prev


def reverse_list_recursive(head: 'ListNode') -> 'ListNode':
    # 为什么你学不会递归？告别递归，谈谈我的一些经验
    # https://mp.weixin.qq.com/s/mJ_jZZoak7uhItNgnfmZvQ

    # if head == None:
    # 原本的條件如上
    # 沒有考慮到 head.next
    # 應該注意到, 更下方的程式邏輯
    # 有使用到 head.next
    # 所以必須提前判斷
    if head == None or head.next == None:
        return head

    # 務必要看解說的網站 之 尋找等價關係
    # 如何思考
    list_1 = reverse_list_recursive(head.next)
    next = head.next
    head.next = None
    next.next = head

    return list_1


if __name__ == '__main__':
    link1 = create_example_linklist(False)
    link2 = create_example_linklist(False)
    traversal_linklist(link1)

    link1 = reverse_list_iterative(link1)
    traversal_linklist(link1)

    link2 = reverse_list_recursive(link2)
    traversal_linklist(link2)
