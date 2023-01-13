import bisect


def left_bound(data: list[int], target: int) -> int:
    # 1. 保证目标在搜索区间[l,r]内
    # 2. 把 0000???111畫出來, 要回傳最後一個true還是第一個false (或 最後一個false還是第一個true
    # 3. 想清楚分界線是什麼, 我們要的是分界線左邊還是右邊那個
    # 4. 每次待查找序列的範圍必須變小

    # check: data[mid] >= target, 搜尋後, 回傳第一個true
    # data 數列, 藉由 check 可以表示為 FFFTTT
    ans = 0
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] >= target:  # [mid,right]
            ans = mid
            right = mid - 1  # [left, mid-1]
        else:
            left = mid + 1

    # https://labuladong.github.io/algo/2/20/30/
    #
    # 当目标元素 target 不存在数组 nums 中时，搜索左侧边界的二分搜索的返回值可以做以下几种解读
    #
    # 1、返回的这个值是 nums 中大于等于 target 的最小元素索引。
    # 2、返回的这个值是 target 应该插入在 nums 中的索引位置。
    # 3、返回的这个值是 nums 中小于 target 的元素个数。
    #
    # 比如在有序数组 nums = [2,3,5,7] 中搜索 target = 4，搜索左边界的二分算法会返回 2，你带入上面的说法，都是对的。

    # 可以選擇把 ans 交給呼叫者判斷, 不給 -1
    # 這樣應用的情境比較多, 如上面的敘述, 都適合用 left bound
    return ans
    # return ans if data[ans] == target else -1


def right_bound(data: list[int], target: int) -> int:
    # 1. 保证目标在搜索区间[l,r]内
    # 2. 把 0000???111畫出來, 要回傳最後一個true還是第一個false (或 最後一個false還是第一個true
    # 3. 想清楚分界線是什麼, 我們要的是分界線左邊還是右邊那個
    # 4. 每次待查找序列的範圍必須變小

    # check 格式 和 find_le 一樣, 但 return 條件不同
    # check: data[mid] <= target, 搜尋後, 回傳最後一個true
    # data 數列, 藉由 check 可以表示為 TTTFFF
    ans = 0
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] <= target:  # [left,mid]
            ans = mid
            left = mid + 1  # [mid+1, right]
        else:
            right = mid - 1

    return ans
    # return ans if data[ans] == target else -1


def find_ge(data: list[int], target: int) -> int:
    # 1. 保证目标在搜索区间[l,r]内
    # 2. 把 0000???111畫出來, 要回傳最後一個true還是第一個false (或 最後一個false還是第一個true
    # 3. 想清楚分界線是什麼, 我們要的是分界線左邊還是右邊那個
    # 4. 每次待查找序列的範圍必須變小

    # check: data[mid] >= target, 搜尋後, 回傳第一個true
    # data 數列, 藉由 check 可以表示為 FFFTTT
    ans = 0
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] >= target:  # [mid,right]
            ans = mid
            right = mid - 1  # [left, mid-1]
        else:
            left = mid + 1
    return ans if data[ans] >= target else -1


def find_gt(data: list[int], target: int) -> int:
    # 1. 保证目标在搜索区间[l,r]内
    # 2. 把 0000???111畫出來, 要回傳最後一個true還是第一個false (或 最後一個false還是第一個true
    # 3. 想清楚分界線是什麼, 我們要的是分界線左邊還是右邊那個
    # 4. 每次待查找序列的範圍必須變小

    # check: data[mid] > target, 搜尋後, 回傳第一個true
    # data 數列, 藉由 check 可以表示為 FFFTTT
    ans = 0
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] > target:  # [mid,right]
            ans = mid
            right = mid - 1  # [left, mid-1]
        else:
            left = mid + 1
    return ans if data[ans] > target else -1


def find_le(data: list[int], target: int) -> int:
    # 1. 保证目标在搜索区间[l,r]内
    # 2. 把 0000???111畫出來, 要回傳最後一個true還是第一個false (或 最後一個false還是第一個true
    # 3. 想清楚分界線是什麼, 我們要的是分界線左邊還是右邊那個
    # 4. 每次待查找序列的範圍必須變小

    # check 格式 和 right_bound 一樣, 但 return 條件不同
    # check: data[mid] <= target, 搜尋後, 回傳最後一個true
    # data 數列, 藉由 check 可以表示為 TTTFFF
    ans = 0
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] <= target:  # [left,mid]
            ans = mid
            left = mid + 1  # [mid+1, right]
        else:
            right = mid - 1
    return ans if data[ans] <= target else -1


def find_lt(data: list[int], target: int) -> int:
    # 1. 保证目标在搜索区间[l,r]内
    # 2. 把 0000???111畫出來, 要回傳最後一個true還是第一個false (或 最後一個false還是第一個true
    # 3. 想清楚分界線是什麼, 我們要的是分界線左邊還是右邊那個
    # 4. 每次待查找序列的範圍必須變小

    # check: data[mid] < target, 搜尋後, 回傳最後一個true
    # data 數列, 藉由 check 可以表示為 TTTFFF
    ans = 0
    left, right = 0, len(data) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] < target:  # [left,mid]
            ans = mid
            left = mid + 1  # [mid+1, right]
        else:
            right = mid - 1
    return ans if data[ans] < target else -1


def binary_search(data: list[int], target: int) -> int:
    # https://labuladong.github.io/algo/2/20/29/
    # https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1

    left = 0
    right = len(data) - 1

    while left <= right:
        mid = left + (right - left) // 2

        current = data[mid]
        if current == target:
            return mid
        elif current < target:
            left = mid + 1
        elif current > target:
            right = mid - 1

    # 問題不在開閉區間, 問題在終止條件
    # 開閉區間只是讓你方便決定終止條件
    # **真正重要的是當你二分搜停下來後指到的東西意義是什麼**

    return -1


if __name__ == '__main__':
    # print(find_gt([1, 2, 2, 2, 4], 0))
    # print(find_gt([1, 2, 2, 2, 4], 5))
    # print(find_gt([1, 2, 2, 2, 4], 3))
    # print(find_gt([1, 2, 2, 2, 4], 2))
    # print(find_gt([1, 2, 2, 2, 4], 4))
    # print()
    #
    # print(find_ge([1, 2, 2, 2, 4], 0))
    # print(find_ge([1, 2, 2, 2, 4], 5))
    # print(find_ge([1, 2, 2, 2, 4], 3))
    # print(find_ge([1, 2, 2, 2, 4], 2))
    # print(find_ge([1, 2, 2, 2, 4], 4))
    print()

    print("left", bisect.bisect_left([1, 2, 2, 2, 4], 2))
    print("left", left_bound([1, 2, 2, 2, 4], 2))
    print("right", bisect.bisect_right([1, 2, 2, 2, 4], 2))
    print("right", right_bound([1, 2, 2, 2, 4], 2))
