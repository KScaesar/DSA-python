from typing import List


class Solution:
    # https://leetcode.com/problems/maximum-product-subarray/

    # 類似題目?
    # 0053. Maximum Subarray

    def maxProduct_dp(self, nums: List[int]) -> int:
        # https://github.com/halfrost/LeetCode-Go/blob/master/leetcode/0152.Maximum-Product-Subarray/README.md
        # https://github.com/apachecn/apachecn-algo-zh/blob/master/docs/leetcode/python/152._maximum_product_subarray.md

        # https://leetcode.com/problems/maximum-product-subarray/solutions/48230/possibly-simplest-solution-with-o-n-time-complexity/
        # multiplied by a negative makes big number smaller, small number bigger
        #         if (A[i] < 0)
        #             swap(iMax, iMin);

        size = len(nums)
        dp_max = [0] * size
        dp_min = [0] * size

        # base case
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, size):
            dp_max[i] = max(dp_max[i - 1] * nums[i], nums[i],  # 到這個地方為止, 轉移函數類似 0053. Maximum Subarray
                            dp_min[i - 1] * nums[i])
            dp_min[i] = min(dp_min[i - 1] * nums[i], nums[i],
                            dp_max[i - 1] * nums[i])

        print(f' dp_max={dp_max}\n dp_min={dp_min}')
        return max(dp_max)

    def maxProduct_dp_fail(self, nums: List[int]) -> int:
        # 嘗試自己想 dp 轉移函數
        # 失敗了, 不想花太多時間

        # dp[x] 0~x 之間的相乘最大值
        dp = [0] * len(nums)

        # dp_negative[x] 包含 x, 之前的元素相乘 有負號 的相乘絕對值最大值
        # 如果 包含 x, 之前的元素相乘 沒有負號, 欄位為 零
        dp_negative = [0] * len(nums)

        # base case
        if nums[0] >= 0:
            dp[0] = nums[0]
        else:
            dp_negative = abs(nums[0])

        for i in range(1, len(nums)):
            if dp_negative == 0 and nums[i] >= 0:
                dp[i] = dp[i - 1] * nums[i]
            elif dp_negative == 0 and nums[i] < 0:
                dp_negative[i] = dp[i - 1] * abs(nums[i])
                dp[i] = nums[i]
            elif dp_negative > 0 and nums[i] >= 0:
                pass
            elif dp_negative > 0 > nums[i]:
                pass

        pass

    def maxProduct_backtrack_fail(self, nums: List[int]) -> int:
        # 原本以為可以用子集合的概念求解
        # 但發現 子集合 不講求順序
        # 而題目要求 子字串 有排序需求

        size = len(nums)
        if size == 0:
            return 0
        ans = nums[0]

        def backtrack(nums, start, track):
            nonlocal ans
            ans = max(ans, track)

            for i in range(start, size):
                backtrack(nums, i + 1, track * nums[i])

        backtrack(nums, 0, 1)
        return ans


if __name__ == '__main__':
    # print(Solution().maxProduct_dp([2, 3, -2, 4]))
    print(Solution().maxProduct_dp([2, 3, -2, 4, -5]))
