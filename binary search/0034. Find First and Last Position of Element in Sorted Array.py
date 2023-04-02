from typing import Callable


class Solution:
    # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0: return [-1, -1]

        return [left_bound_v2(nums, target), right_bound_v2(nums, target)]

    def searchRange_lambda(self, nums: list[int], target: int) -> list[int]:
        if len(nums) == 0: return [-1, -1]

        left_bound = lambda mid_value, target: mid_value >= target
        right_bound = lambda mid_value, target: mid_value <= target

        # 以下兩者同等意義, 只是需要帶入的 check function 不同
        # binary_search_by_FFFTTT_ans_on_true_side
        # binary_search_by_TTTFFF_ans_on_false_side
        return [
            binary_search_by_FFFTTT_ans_on_true_side(nums, target, left_bound),
            binary_search_by_TTTFFF_ans_on_true_side(nums, target, right_bound),
        ]


#    ↓
# FFFTTT
def binary_search_by_FFFTTT_ans_on_true_side(nums: list[int], target: int, check_fn: Callable[[int, int], bool]) -> int:
    l, r = 0, len(nums) - 1
    ans = 0

    while l <= r:
        mid = (l + r) // 2
        if check_fn(nums[mid], target):
            r = mid - 1
            ans = mid
        else:
            l = mid + 1

    return ans if nums[ans] == target else -1


#   ↓
# TTTFFF
def binary_search_by_TTTFFF_ans_on_true_side(nums: list[int], target: int, check_fn: Callable[[int, int], bool]) -> int:
    l, r = 0, len(nums)
    ans = 0

    while l < r:
        mid = (l + r) // 2
        if check_fn(nums[mid], target):
            l = mid + 1
            ans = mid
        else:
            r = mid

    return ans if nums[ans] == target else -1


#    ↓
# TTTFFF
def binary_search_by_TTTFFF_ans_on_false_side(nums: list[int], target: int, check_fn: Callable[[int, int], bool]) -> int:
    l, r = 0, len(nums)
    ans = 0

    while l < r:
        mid = (l + r) // 2
        if check_fn(nums[mid], target):
            l = mid + 1
        else:
            ans = mid
            r = mid

    return ans if nums[ans] == target else -1


def left_bound_v1(nums: list[int], target: int):
    l, r = 0, len(nums) - 1
    ans = 0

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans if nums[ans] == target else -1


def left_bound_v2(nums: list[int], target: int):
    l, r = 0, len(nums)
    ans = 0

    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            ans = mid
            r = mid
        else:
            l = mid + 1

    return ans if nums[ans] == target else -1


def right_bound_v1(nums: list[int], target: int):
    l, r = 0, len(nums) - 1
    ans = 0

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans if nums[ans] == target else -1


def right_bound_v2(nums: list[int], target: int):
    l, r = 0, len(nums)
    ans = 0

    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            ans = mid
            l = mid + 1
        else:
            r = mid

    return ans if nums[ans] == target else -1


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange_lambda([5, 7, 7, 8, 8, 10], 8))
