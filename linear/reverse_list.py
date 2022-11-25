from tool import *


def reverse_list_iterative(head: 'ListNode') -> ListNode | None:
    if head == None:
        return None

    _next: 'ListNode' = None
    cursor: 'ListNode' = head
    prev: 'ListNode' = None

    while cursor:
        _next = cursor.next
        cursor.next = prev
        prev = cursor
        cursor = _next

    return prev


# @debugHelper
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
    _next = head.next
    head.next = None
    _next.next = head

    return list_1


if __name__ == '__main__':
    head1, _ = create_linklist_from_array([2, 4, 6, 3, 7])
    print('list1 = ', traversal_linklist(head1), '\n')
    rLink1 = reverse_list_iterative(head1)
    print(traversal_linklist(rLink1), '\n')

    head2, _ = create_linklist_from_array([2, 4, 6, 3, 7])
    print('list2 = ', traversal_linklist(head2), '\n')
    rLink2 = reverse_list_recursive(head2)
    print(traversal_linklist(rLink2), '\n')
