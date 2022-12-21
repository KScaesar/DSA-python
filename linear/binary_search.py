def binary_search(data: list[int], target: int) -> int:
    # https://labuladong.github.io/algo/2/20/29/
    # https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1

    # 因為把 right 定義為 len-1
    # 可得搜尋區間 = [left, right]
    #
    # 若把 right 定義為 len
    # 搜尋區間 = [left, right) 避免索引越界
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # print('before', left, right, mid)

        current = data[mid]
        if current == target:
            return mid
        elif current < target:
            left = mid + 1
        elif current > target:
            right = mid - 1

        # print('after', left, right, mid)

    # 問題不在開閉區間, 問題在終止條件
    # 開閉區間只是讓你方便決定終止條件
    # **真正重要的是當你二分搜停下來後指到的東西意義是什麼**
    #
    # 在一般的二分搜尋
    # left=0
    # right=len-1
    # while left < right [left, right)
    #
    # 迴圈結束後, 會少比較最後一個數值
    # 不能直接認定 left == target
    # 需要在迴圈外 比較最後一次

    return -1


# https://labuladong.github.io/algo/2/20/30/
#
# 当目标元素 target 不存在数组 nums 中时，搜索左侧边界的二分搜索的返回值可以做以下几种解读
#
# 1、返回的这个值是 nums 中大于等于 target 的最小元素索引。
# 2、返回的这个值是 target 应该插入在 nums 中的索引位置。
# 3、返回的这个值是 nums 中小于 target 的元素个数。
#
# 比如在有序数组 nums = [2,3,5,7] 中搜索 target = 4，搜索左边界的二分算法会返回 2，你带入上面的说法，都是对的。
def left_bound(data: list[int], target: int) -> int:
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # print(left, right, mid)

        current = data[mid]
        if current == target:
            right = mid - 1  # 改 right
        elif current < target:
            left = mid + 1
        elif current > target:
            right = mid - 1

    # 回傳 left
    # 重點 left bound 需要檢查是否 大於 n
    # leetcode 34
    return -1 if left >= len(data) or data[left] != target else left


def right_bound_fail(data: list[int], target: int) -> int:
    left = 0
    right = len(data) - 1

    while left < right:
        mid = left + (right - left) // 2
        # print(left, right, mid)

        current = data[mid]
        if current == target:
            # 計算 mid, 除以2的特性, 得到的數值會往小數值靠近
            # left=0, right=1 -> mid=0
            # >> if not plus 0: left=mid=0, left 維持不動
            # 變成無窮迴圈
            #
            # left 要往右邊靠近
            # 需要另外 + 1, 但若進行 +1 運算
            # 要考慮分別考慮不同情況
            #
            # 1. 正常的前進一步
            # left=0, right=1 -> mid=0
            # left=mid+1=1
            #
            # 2. 多走一步
            # left=1, right=3 -> mid=2
            # left=mid+1=3
            left = mid + 1
        elif current < target:
            left = mid + 1
        elif current > target:
            right = mid - 1

    return right - 1 if data[right - 1] == target else -1


def right_bound(data: list[int], target: int) -> int:
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # print(left, right, mid)

        current = data[mid]
        if current == target:
            left = mid + 1
        elif current < target:
            left = mid + 1
        elif current > target:
            right = mid - 1

    # 重點 right bound 需要檢查是否 小於 0
    # leetcode 34
    return -1 if right < 0 or data[right] != target else right


if __name__ == '__main__':
    print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 1))
    print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 40))
    print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 50))
    print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], -1))
    print()
    # print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 1))
    # print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 6))
    # print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 7))
    # print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 4))
    # print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], -2))
    # print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 3))
    # print()
    # print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 1))
    # print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 6))
    # print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 7))
    # print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 4))
    # print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], -2))
    # print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 3))
