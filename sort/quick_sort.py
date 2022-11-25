from tool import *


# 需要返回 pivot index
# 所以不能直接傳入一個縮小的陣列
# 需要使用額外參數 描述陣列大小
def partition_array(nums: list[int], left: int, right: int) -> int:
    # 不需要這個條件
    # 即使需要, 也不應該回傳 0
    # 再次重複 陣列大小是 left right 決定
    # pivot 一定在 left right 之間
    # 直接回傳 0 肯定是錯誤錯法
    # if left == right:
    #     return 0

    # 錯誤作法, 即使先排序左邊 保證 mid 是最大值
    # 但右邊可能有數字比左邊小
    # 右邊並非全部都大於 num[mid]
    #
    # mid = left + (right - left) // 2
    # for i in range(left, right + 1):
    #     if (i < mid and nums[i] > nums[mid]) or (i > mid and nums[i] < nums[mid]):
    #         nums[i], nums[mid] = nums[mid], nums[i]

    # https://youtu.be/Dk9tpG6Jhso?list=PLl-9hEcChubjZRzIoSdACioC2Fsx-JBup&t=120
    pivot = nums[left]
    while left < right:

        # 若 pivot 選第一個, 此處一定要先從 最右判斷大小
        # 不能先判斷左邊
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        # print(left, right)

        while left < right and nums[left] <= pivot:
            left += 1
        nums[right] = nums[left]
        # print(left, right)

    nums[left] = pivot

    return left


def partition_linklist(head: ListNode, tail: ListNode) -> tuple[ListNode | None, ListNode | None]:
    # https://selfboot.cn/2016/09/01/lost_partition/
    # https://gist.github.com/ytaminE/d2ff709cef397373188dcb421cc12975
    #
    # 分組運算的時間複雜度 O(n)

    # 最好在 partition_linklist 的呼叫端
    # 就確保 head and tail is not None
    if head is None and tail is None:
        return None, None
    if head is None or tail is None:
        pivot = head if head is not None else tail
        return None, pivot

    pivot = head
    slow = head
    fast = head.next  # 不需要判斷 pivot 自身, 所以直接跳過

    # 由於 quick sort 選出 pivot 以後
    # 就會排除 pivot
    # 對左右側數列, 進行再次分割
    # 而 link list 的特性, 無法知道 前一個 node
    # 所以最好回傳 prev_pivot 當作 左側數列的 tail 節點
    #
    # 再次想想 感覺不太對
    # 如果 遞迴到一半 切割的數列
    # 是中間部份只有兩個元素的數列
    # 即使以小區段的數列來看, 確實 prev_pivot 可能為 None
    # 但以整體數列 是存在 prev_pivot
    #
    # 最好的作法
    # 可能還是需要 每次都從 原始數列的開頭進行邏輯判斷
    # https://www.geeksforgeeks.org/quicksort-on-singly-linked-list/
    prev_pivot: ListNode | None = None

    while fast != tail.next:  # head 到 tail 所有元素都要進行判斷
        if fast.value < pivot.value:  # 慢指針的前進條件
            prev_pivot = slow
            slow = slow.next
            if slow != fast:  # 快慢指針 指向不同節點, 才需要交換
                slow.value, fast.value = fast.value, slow.value

        fast = fast.next

    slow.value, pivot.value = pivot.value, slow.value  # 最後一步交換, 才讓 slow 真正具有 pivot 特徵

    # 由於 prev_pivot 可能為 None
    # 因此需要 pivot 來找尋 右側數列的 head 節點
    return prev_pivot, slow


def quick_sort(nums: list[int]):
    # 另外提供簡單好懂的寫法, 但需要較多記憶體空間
    # https://go.dev/play/p/GXxAXKWtwk_B

    @debug_helper
    def _sort(nums: list[int], left: int, right: int):
        # 和 merge_sort_v2 進行比較
        # 兩個程式碼位置相同, 邏輯判斷不相同
        if left >= right:
            return

        pivot = partition_array(nums, left, right)
        _sort(nums, left, pivot - 1)  # 注意 不要寫成 _sort(nums, 0, pivot - 1)
        _sort(nums, pivot + 1, right)

    _sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    # input1 = [2, 3, 9, 1, 7, 4]
    # input1 = [2, 5, 3, 4, 1]
    # input1 = [5, 9, 2, 1, 4, 7, 5, 8, 3, 6]
    # sol1 = partition_array(input1, 0, len(input1) - 1)
    # print(f'{partition_array.__name__} = {input1}, (index={sol1}, value={input1[sol1]})\n')

    input2 = [5, 9, 2, 1, 4, 7, 5, 8, 3, 6]
    head2, tail2 = create_linklist_from_array(input2)
    sol2 = partition_linklist(head2, tail2)
    print(f'{partition_linklist.__name__} = {traversal_linklist(head2)}, {[(id(x.value), x.value) for x in list(sol2)]}\n')

    input3 = [5, 9, 2, 1, 4, 7, 5, 8, 3, 6]
    # input3 = [9, 8]
    # input3 = [8, 9]
    quick_sort(input3)
    print(f'{quick_sort.__name__} = {input3}\n')
