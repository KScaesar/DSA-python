from tool import debug_helper, ListNode, create_linklist_from_array, traversal_linklist


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
        if list1.val >= list2.val:
            cursor.next = list2
            list2 = list2.next
            cursor = cursor.next
        elif list1.val < list2.val:
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


def merge_sort_v1(nums: list[int]) -> list[int]:
    # 兩個以上才需要分割, if len(nums) == 0 是錯誤條件
    #
    # 直接傳子陣列 有可能出現 陣列大小為 0 的情況
    # 與 merge_sort_v2 不一樣
    # 要好好比較
    if len(nums) < 2:
        return nums

    # left = 0
    # right = len(nums) - 1
    # mid = left + (right - left) // 2
    #
    # 如果取中值 用上面的方式
    # 分割數列的時候 mid 要記得 +1, 不然會進入無窮迴圈
    # 比如剩下兩個元素 len=2, left=0, right=1 -> get mid=0
    # 若分割數列的方式為 nums[:mid]
    # 無法把兩個元素分割, 會一直切成 0個 2個
    #
    # n1 = merge_sort(nums[:mid + 1])
    # n2 = merge_sort(nums[mid + 1:])

    mid = len(nums) // 2
    n1 = merge_sort_v1(nums[:mid])
    n2 = merge_sort_v1(nums[mid:])

    return merge_array_v1(n1, n2)


@debug_helper
def merge_sort_v2_fail(nums: list[int]):
    if len(nums) < 2:
        return

    left = 0
    right = len(nums) - 1
    left_end = len(nums) // 2

    # 如果想要 in place 排序 nums
    # 第一個參數 不應該改變大小
    # 要加上其他參數 來形容 陣列大小
    merge_sort_v2_fail(nums[:left_end + 1])
    merge_sort_v2_fail(nums[left_end + 1:])
    merge_array_v2(nums, left, left_end, right)
    return


def merge_sort_v2(nums: list[int]):
    # 表達一個陣列目前的大小
    # 利用 最左 和 最右

    # @debug_helper
    def _sort(nums: list[int], left: int, right: int):
        # 搞清楚結束條件, if right - left < 2 是錯誤條件
        # 和 quick sort 進行比較
        # 兩個程式碼位置相同, 邏輯判斷不相同
        #
        # 用游標表示陣列大小
        # 不會出現 大小為0的情況
        # 所以只要判斷剩下1個元素
        # 就可以 return
        if right == left:
            return

        # 注意 現在 left right 的來源 是 參數
        # 不是 nums, 不需要自己重新定義
        #
        # left = 0
        # right = len(nums) - 1
        # left_end = len(nums) // 2

        mid = left + (right - left) // 2

        _sort(nums, left, mid)
        _sort(nums, mid + 1, right)
        merge_array_v2(nums, left, mid, right)

        return

    _sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    input1 = [2, 4, 3, 6, 1, 2, 9]
    sol1 = merge_sort_v1(input1)
    print(f'{merge_sort_v1.__name__} = {sol1}\n')

    input2 = [2, 4, 3, 6, 1, 2, 9]
    merge_sort_v2(input2)
    print(f'{merge_sort_v2.__name__} = {input2}\n')

    ###

    sol3 = merge_array_v1([2, 3, 4], [1, 1, 3, 5, 7])
    print(f'{merge_array_v1.__name__} = {sol3}\n')

    input4 = [2, 3, 4, 1, 1, 3, 5, 7]
    merge_array_v2(input4, 0, 2, 7)
    print(f'{merge_array_v2.__name__} = {input4}\n')

    head1, _ = create_linklist_from_array([2, 3, 4])
    head2, _ = create_linklist_from_array([1, 1, 3, 5, 7])
    sol5 = merge_linklist(head1, head2)
    print(f'{merge_linklist.__name__} = {traversal_linklist(sol5)}\n')
