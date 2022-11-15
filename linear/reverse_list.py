from model import ListNode
import cycle


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
    head1 = cycle.create_example_linklist(False)
    head2 = cycle.create_example_linklist(False)
    cycle.traversal(head1)

    head1 = reverse_list_iterative(head1)
    cycle.traversal(head1)

    head2 = reverse_list_recursive(head2)
    cycle.traversal(head2)
