from typing import List


class Solution:
    # https://leetcode.com/problems/product-of-array-except-self/
    def productExceptSelf_v3(self, nums: List[int]) -> List[int]:
        # Follow up: Can you solve the problem in O(1) extra space complexity

        size = len(nums)
        ans = [1] * size  # 初始化為 1, 就不需要處理 v2 的邊界

        prefix = 1
        for i in range(size):
            ans[i] = prefix
            prefix *= nums[i]

        last = size - 1
        suffix = 1
        for i in range(last, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans

    def productExceptSelf_v2(self, nums: List[int]) -> List[int]:
        # Follow up: Can you solve the problem in O(1) extra space complexity

        size = len(nums)
        ans = [0] * size

        prefix = 0
        for i in range(1, size):
            if i == 1:
                prefix = nums[0]
            else:
                prefix *= nums[i - 1]
            ans[i] = prefix

        last = size - 1
        suffix = 0
        for i in range(last - 1, -1, -1):
            if i == last - 1:
                suffix = nums[last]
            else:
                suffix *= nums[i + 1]

            if i == 0:
                ans[i] = suffix
            else:
                ans[i] *= suffix

        return ans

    def productExceptSelf_v1(self, nums: List[int]) -> List[int]:
        size = len(nums)

        prefix = [0] * size
        prefix[0] = nums[0]
        for i in range(1, size):
            prefix[i] = prefix[i - 1] * nums[i]

        suffix = [0] * size
        suffix[-1] = nums[-1]
        for i in range(size - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        ans = [0] * size
        for i in range(size):
            if i == 0:
                ans[i] = suffix[i + 1]
            elif i == size - 1:
                ans[i] = prefix[i - 1]
            else:
                ans[i] = prefix[i - 1] * suffix[i + 1]

        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf_v3([-1, 1, 0, -3, 3]))
