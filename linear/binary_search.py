def binary_search(data: list[int], target: int) -> int:
    # 因為把 right 定義為 len-1
    # 可得搜尋區間 = [left, right]
    #
    # 若把 right 定義為 len
    # 搜尋區間 = [left, right) 避免索引越界
    left = 0
    right = len(data)-1

    while left <= right:
        mid = left+(right-left)//2
        # print('before', left, right, mid)

        current = data[mid]
        if current == target:
            return mid
        elif current < target:
            left = mid+1
        elif current > target:
            right = mid-1

        # print('after', left, right, mid)

    return -1


def left_bound(data: list[int], target: int) -> int:
    left = 0
    right = len(data)-1

    while left <= right:
        mid = left+(right-left)//2
        # print(left, right, mid)

        current = data[mid]
        if current == target:
            right = mid-1
        elif current < target:
            left = mid+1
        elif current > target:
            right = mid-1

    return -1 if left >= len(data) or data[left] != target else left


def right_bound_fail(data: list[int], target: int) -> int:
    left = 0
    right = len(data)-1

    while left < right:
        mid = left+(right-left)//2
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
            left = mid+1
        elif current < target:
            left = mid+1
        elif current > target:
            right = mid-1

    return right-1 if data[right-1] == target else -1


def right_bound(data: list[int], target: int) -> int:
    left = 0
    right = len(data)-1

    while left <= right:
        mid = left+(right-left)//2
        # print(left, right, mid)

        current = data[mid]
        if current == target:
            left = mid+1
        elif current < target:
            left = mid+1
        elif current > target:
            right = mid-1

    return -1 if right < 0 or data[right] != target else right

# 所有元素的數值 必須是唯一的, 不可重複
# search 和 sort 是密不可分的
# search 演算法 都是基於 已經排序好的資料 進行 search
#
# 一般來說有幾個指標會讓你直接想到二分搜尋
# 1. 排序後的數組
# 2. 限定時間複雜度的搜尋法(比方說題目限定O(n)以下的解法)
#
# https://blog.csdn.net/pegasuswang_/article/details/18402767


if __name__ == '__main__':
    # print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 1))
    # print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 40))
    # print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 50))
    # print('binary_search ans =', binary_search([1, 4, 5, 9, 20, 40, 60], -1))
    print()
    print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 1))
    print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 6))
    print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 7))
    print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 4))
    print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], -2))
    print('left_bound ans =', left_bound([1, 3, 3, 3, 3, 6], 3))
    print()
    print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 1))
    print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 6))
    print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 7))
    print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 4))
    print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], -2))
    print('right_bound ans =', right_bound([1, 3, 3, 3, 3, 6], 3))
