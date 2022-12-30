from typing import List


class Solution:
    # https://leetcode.com/problems/house-robber/

    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        # dp[i]：考虑下标i（包括i）以内的房屋，最多可以偷窃的金额为dp[i]
        dp = [0] * size

        # base
        if size >= 1:
            dp[0] = nums[0]
        if size >= 2:
            dp[1] = max(nums[1], dp[0])

        for i in range(2, size):
            dp[i] = max(
                dp[i - 2] + nums[i],  # 搶劫這家
                dp[i - 1]  # 不搶劫
            )

        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2, 1, 1, 2]))
