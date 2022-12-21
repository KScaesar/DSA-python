from typing import List


class Solution:
    # https://leetcode.com/problems/search-in-rotated-sorted-array/
    #
    # https://hackmd.io/DVBrXRmSS2ihGcEafScwcw#33-Search-in-Rotated-Sorted-Array
    #
    # mid 切一半的情況, 一定會存在 一邊正常排序, 一邊不正常排序
    # 每次對切都判斷這兩種情況
    # https://goplay.tools/snippet/l9eFYcpGLp5
    #
    # https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/14436/revised-binary-search/?orderBy=most_votes

    def search_v3(self, nums: List[int], target: int) -> int:
        def helper(nums: List[int], start: int, end: int, target: int) -> int:
            left = start
            right = end

            while left <= right:
                mid = left + (right - left) // 2
                print(left, right, mid)
                if nums[mid] == target:
                    return mid

                if nums[mid] > nums[right]:  # 右側異常
                    if nums[left] <= target < nums[mid]:  # 如果 target 的範圍在左側
                        right = mid - 1
                    else:  # 如果不在左側, 就往右邊尋找

                        # 以下兩個寫法都正確
                        left = mid + 1
                        # return helper(nums, mid + 1, right, target)

                else:  # 左側異常
                    if nums[mid] < target <= nums[right]:  # 如果 target 的範圍在右側
                        left = mid + 1
                    else:
                        # 以下兩個寫法都正確
                        right = mid - 1
                        # return helper(nums, left, mid - 1, target)

            return -1

        def helper_fail(nums: List[int], start: int, end: int, target: int) -> int:
            # 兩種判斷方式 都有部份情境會失敗, ex: nums=[3,1] target=1
            # 1. 先判斷是否正常排序的區段, 再進行二分搜尋
            # 2. 先進行二分搜尋, 再判斷是否正常排序的區段

            left = start
            right = end

            while left <= right:
                mid = left + (right - left) // 2
                print(left, right, mid)
                if nums[mid] == target:
                    return mid

                if nums[mid] > nums[right]:  # 右側異常
                    if target < nums[mid]:  # 搜尋左側
                        right = mid - 1
                    elif nums[mid] < target:  # 搜尋右側
                        return helper_fail(nums, mid + 1, right, target)
                else:  # 左側異常
                    if target < nums[mid]:  # 搜尋左側
                        return helper_fail(nums, left, mid - 1, target)
                    elif nums[mid] < target:  # 搜尋右側
                        left = mid + 1

            return -1

        return helper(nums, 0, len(nums) - 1, target)

    def search_v2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo = 0
        hi = n - 1

        # 分為左右兩個區段, 檢查其中一個區段, 來判斷該區段是否為 正常排序
        # 1. nums[0, …, mid-1]
        # 2. nums[mid, …, length - 1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # if nums[lo] < nums[mid - 1]:
            # 只能用 右區段判斷
            # 用左區段 答案是錯誤的
            # 原因不明
            # https://leetcode.wang/leetcode-153-Find-Minimum-in-Rotated-Sorted-Array.html
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        offset = lo
        # print("offset", offset)

        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            offset_mid = move_offset(mid, offset, n)
            if nums[offset_mid] == target:
                return offset_mid
            elif nums[offset_mid] > target:
                hi = mid - 1
            elif nums[offset_mid] < target:
                lo = mid + 1

        return -1

    def search_timeout(self, nums: List[int], target: int) -> int:
        # 原本的想法
        # 1. 想先找出 偏移點的位置
        # 2. 依照 nums 原本的索引位置 + 偏移位置, 利用某種關係公式 找到目標索引
        # 但第一步驟就卡住, 想不到如何用 O(logN) 的 複雜度, 找出旋轉點
        #
        # 第一步驟暫時用 O(N) 求得
        # 先嘗試找出第二步驟的關係公式
        # 雖然可以正確求解
        # 但 leetocde 會 timeout

        n = len(nums)

        # 第一步驟
        i = 1
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        offset = i if i != len(nums) else 0
        # print("offset", offset)

        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid = move_offset(mid, offset, n)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = move_offset(mid - 1, -offset, n)  # 進行 逆向 offset, 變回 沒經過 offset 的狀態
            elif nums[mid] < target:
                lo = move_offset(mid + 1, -offset, n)

        return -1


def move_offset(cursor: int, offset, size) -> int:
    # offset 輸入負號
    # 造成最後索引變成負值
    # 在其他語言會造成錯誤, 因此加上 size 保持為正號
    return (cursor + (size + offset)) % size


if __name__ == '__main__':
    # print(f'{Solution().search_timeout([4, 5, 6, 7, 0, 1, 2], 0)}')
    # print(f'{Solution().search_timeout([4, 5, 6, 7, 0, 1, 2], 4)}')
    # print(f'{Solution().search_timeout([4, 5, 6, 7, 0, 1, 2], 2)}')
    # print(f'{Solution().search_timeout([4, 5, 6, 7, 0, 1, 2], 3)}')
    # print(f'{Solution().search_timeout([1, 3], 1)}')
    # print(f'{Solution().search_timeout([3, 1], 1)}')
    print()

    # print(f'{Solution().search_v2([4, 5, 6, 7, 0, 1, 2], 0)}')
    # print(f'{Solution().search_v2([4, 5, 6, 7, 0, 1, 2], 4)}')
    # print(f'{Solution().search_v2([4, 5, 6, 7, 0, 1, 2], 2)}')
    # print(f'{Solution().search_v2([4, 5, 6, 7, 0, 1, 2], 3)}')
    # print(f'{Solution().search_v2([1, 3], 1)}')
    # print(f'{Solution().search_v2([3, 1], 1)}')
    # print(f'{Solution().search_v2([3, 1, 2], 1)}')
    print()

    # print(f'{Solution().search_v2([4, 5, 6, 7, 0, 1, 2], 5)}')
    # print(f'{Solution().search_v3([1, 3], 1)}')
    print(f'{Solution().search_v3([3, 1], 1)}')
    # print(f'{Solution().search_v3([3, 1, 2], 1)}')
    print()

    # 測試 offset 兩次
    # 是否會變回 原本的數值
    #
    # i0 = 4
    # i1 = move_offset(i0, 3, 5)
    # i2 = move_offset(i1, 3, 5)
    # print(i0, i1, i2)
