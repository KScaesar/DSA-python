from typing import List


class Solution:
    # https://leetcode.com/problems/contains-duplicate/

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate_v1(self, nums: List[int]) -> bool:
        memo = set()
        for v in nums:
            if v in memo:
                return True
            else:
                memo.add(v)
        return False

    def containsDuplicate_fail(self, nums: List[int]) -> bool:
        # 有可能出現 負號
        # 所以不適合 cyclic sort

        size = len(nums)
        for i in range(size):
            idx = nums[i] - 1
            if nums[idx] - 1 != idx:
                nums[i], nums[idx] = nums[idx], nums[i]
            # print(nums)

        for i in range(size):
            if nums[i] - 1 != i:
                return True
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 2, 3, 4]))
    # print(Solution().containsDuplicate([1, 1, 2, 3]))
    # print(Solution().containsDuplicate([2, 2, 1, 3]))
