from typing import List


class Solution:
    # https://leetcode.com/problems/missing-number/
    def missingNumber_v3(self, nums: List[int]) -> int:
        # 執行兩次 xor

        ans = 0
        for i, v in enumerate(nums):
            ans ^= i
            ans ^= v

        return ans ^ len(nums)

    def missingNumber_v2(self, nums: List[int]) -> int:
        # 執行兩次 xor

        ans = 0
        # 注意 使用 len(nums) + 1 才會把 len(nums) 的情況考慮進去
        # for i in range(len(nums)):
        for i in range(len(nums) + 1):
            ans ^= i
        for v in nums:
            ans ^= v

        return ans

    def missingNumber_v1(self, nums: List[int]) -> int:
        size = len(nums)

        extra = -1
        i = 0

        # 用 range 自動累積 i 的方式
        # 無法確保每個元素在 應該的位置
        # for i in range(size):
        while i < size:
            print(nums, extra)
            idx = nums[i]

            # 重要: 一定要把 -1 放在前面判斷
            # -1 的情況無法把放到正確位置
            if idx == -1:
                i += 1
            elif idx != size and nums[idx] != idx:
                nums[i], nums[idx] = nums[idx], nums[i]
            elif idx == size:
                nums[i], extra = extra, nums[i]
            else:
                i += 1

        print(nums, extra)
        for i in range(size):
            if nums[i] == -1:
                return i

        # 也要檢查最後一個欄位
        if extra == -1:
            return size


if __name__ == '__main__':
    print(Solution().missingNumber_v2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(Solution().missingNumber_v3([3, 0, 1]))
    # print(Solution().missingNumber_v2([0]))
    # print(Solution().missingNumber_v2([1, 2]))

    # print(3 ^ 3 ^ 2 ^ 0)
