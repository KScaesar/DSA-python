from typing import List


class Solution:
    # https://leetcode.com/problems/find-peak-element/

    def findPeakElement_v2(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0

        left = 0
        right = size - 1
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2

            # 如果 mid 较大，则左侧存在峰值
            # 如果 mid + 1 较大，则右侧存在峰值
            if mid != size - 1 and nums[mid] > nums[mid + 1]:
                ans = mid
                right = mid - 1
            elif mid == size - 1 and nums[mid - 1] < nums[mid]:
                return mid
            else:
                left = mid + 1
        return ans

    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return 0

        left = 0
        right = size - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(nums, mid, size):
                return mid
            elif mid != size - 1 and nums[mid] <= nums[mid + 1]:
                left = mid + 1
            elif mid != 0 and nums[mid - 1] >= nums[mid]:
                right = mid - 1
            elif mid == size - 1:
                right = mid - 1
            elif mid == 0:
                left = mid + 1

    def check(self, nums, idx, size) -> bool:
        if 1 <= idx <= size - 2 and nums[idx] > nums[idx - 1] and nums[idx] > nums[idx + 1]:
            return True
        if idx == 0 and nums[idx] > nums[idx + 1]:
            return True
        if idx == size - 1 and nums[idx] > nums[idx - 1]:
            return True
        return False


if __name__ == '__main__':
    print(Solution().findPeakElement([1, 2, 3, 1]))
    print(Solution().findPeakElement_v2([1, 2, 3, 1]))
    print(Solution().findPeakElement_v2([1, 2]))
