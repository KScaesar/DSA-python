from typing import List


class Solution:
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

    # 類似題目
    # 0153. Find Minimum in Rotated Sorted Array
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1

        # left bound
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1

        print('left', lo, hi, len(nums))

        # error
        # if -1 < lo and nums[lo] == target:

        # 算法筆記 p78
        # 應該解讀為 nums 中, 小於 target 的元素有幾個
        if lo < len(nums) and nums[lo] == target:  # 重點 left bound 需要檢查是否 大於 n
            start = lo

        # right bound
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1

        print('right', lo, hi, len(nums))

        # error
        # if hi < len(nums) and nums[hi] == target:

        # 算法筆記 p84
        if -1 < hi and nums[hi] == target:  # 重點 right bound 需要檢查是否 小於 0
            end = hi

        return [start, end]


if __name__ == '__main__':
    print(f'{Solution().searchRange([5, 7, 7, 8, 8, 10], 5)}\n')
    print(f'{Solution().searchRange([5, 7, 7, 8, 8, 10], 11)}\n')
    print(f'{Solution().searchRange([5, 7, 7, 8, 8, 10], 4)}\n')
