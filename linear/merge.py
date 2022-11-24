from tool import *


# 将 nums1 和 nums2 这两个有序数组合并成一个有序数组
def merge_array_v1(nums1: list[int], nums2: list[int]) -> list[int]:
    N1 = len(nums1)
    N2 = len(nums2)
    result: list[int] = [0] * (len(nums1) + len(nums2))

    if N1 == 0 or N2 == 0:
        return nums1 if N1 != 0 else nums2

    i, j, k = 0, 0, 0
    while i < N1 and j < N2:
        if nums1[i] >= nums2[j]:
            result[k] = nums2[j]
            j += 1
            k += 1
        elif nums1[i] < nums2[j]:
            result[k] = nums1[i]
            i += 1
            k += 1

    # 處理某一方数组已全部被合并的情況
    while i != N1 or j != N2:
        if i == N1:
            result[k] = nums2[j]
            j += 1
            k += 1
        elif j == N2:
            result[k] = nums1[i]
            i += 1
            k += 1

    return result


def merge_array_v2(nums: list[int], left: int, left_end: int, right: int):
    # 觀念圖解
    # https://labuladong.github.io/algo/2/21/41/
    # https://labuladong.github.io/algo/images/%e5%bd%92%e5%b9%b6%e6%8e%92%e5%ba%8f/5.jpeg

    # 如果將此函數用到 merge sort
    # 遞迴呼叫 temp 會反覆 創見銷毀 空間
    # 必要的話 可以把 temp 變數
    # 定義在外部 scope
    temp = [x for x in nums]

    i = left
    j = left_end + 1
    k = left

    while i <= left_end and j <= right:
        if temp[i] >= temp[j]:
            nums[k] = temp[j]
            j += 1
            k += 1
        elif temp[i] < temp[j]:
            nums[k] = temp[i]
            i += 1
            k += 1

    while i != left_end + 1 or j != right + 1:
        if i == left_end + 1:
            nums[k] = temp[j]
            j += 1
            k += 1
        elif j == right + 1:
            nums[k] = temp[i]
            i += 1
            k += 1

    return


def merge_linklist(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None or list2 is None:
        return list1 if list1 is not None else list2

    dummy = ListNode(-1)
    cursor = dummy

    while list1 != None and list2 != None:
        if list1.value >= list2.value:
            cursor.next = list2
            list2 = list2.next
            cursor = cursor.next
        elif list1.value < list2.value:
            cursor.next = list1
            list1 = list1.next
            cursor = cursor.next

    if list1 is not None:
        cursor.next = list1
    elif list2 is not None:
        cursor.next = list2

    _next = dummy.next
    dummy.next = None
    return _next


def main():
    sol1 = merge_array_v1([2, 3, 4], [1, 1, 3, 5, 7])
    print(f'{merge_array_v1.__name__} = {sol1}\n')

    input2 = [2, 3, 4, 1, 1, 3, 5, 7]
    merge_array_v2(input2, 0, 2, 7)
    print(f'{merge_array_v2.__name__} = {input2}\n')

    list1 = create_linklist_from_array([2, 3, 4])
    list2 = create_linklist_from_array([1, 1, 3, 5, 7])
    sol3 = merge_linklist(list1, list2)
    print(f'{merge_linklist.__name__} = {traversal_linklist(sol3)}\n')


if __name__ == '__main__':
    main()
