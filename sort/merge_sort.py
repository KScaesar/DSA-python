import linear.merge
from tool import debug_helper


# @debug_helper
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

    return linear.merge.merge_array_v1(n1, n2)


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
    linear.merge.merge_array_v2(nums, left, left_end, right)
    return


def merge_sort_v2(nums: list[int]):
    # 表達一個陣列目前的大小
    # 利用 最左 和 最右

    # @debug_helper
    def _sort(nums: list[int], left: int, right: int):
        # 搞清楚結束條件, if right - left < 2 是錯誤條件
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
        linear.merge.merge_array_v2(nums, left, mid, right)

        return

    _sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    input1 = [2, 4, 3, 6, 1, 2, 9]
    sol1 = merge_sort_v1(input1)
    print(f'{merge_sort_v1.__name__} = {sol1}\n')

    input2 = [2, 4, 3, 6, 1, 2, 9]
    merge_sort_v2(input2)
    print(f'{merge_sort_v2.__name__} = {input2}\n')
