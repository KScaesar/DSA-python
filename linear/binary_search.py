def binary_search(data: list[int], target: int) -> int:
    left = 0
    right = len(data)-1

    # 背下來
    # 寫成 while left <= right 的話
    # 當 target 不存在的時候, 會進入無窮迴圈
    while left < right:
        mid = left+(right-left)//2
        print(left, right, mid)

        if data[mid] > target:
            right = mid
        elif data[mid] < target:
            left = mid+1
        else:
            return mid

    return -1

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
    # print('ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 50))
    # print('ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 40))
    # print('ans =', binary_search([1, 4, 5, 9, 20, 40, 60], 1))
    print('ans =', binary_search([1, 4, 5, 9, 20, 40, 60], -1))
