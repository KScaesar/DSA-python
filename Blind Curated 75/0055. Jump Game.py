from typing import List


class Solution:
    # https://leetcode.com/problems/jump-game/

    # greedy or dp

    def canJump_greedy(self, nums: List[int]) -> bool:
        # 算法筆記 387
        # https://labuladong.github.io/algo/3/29/102/

        # greedy

        n = len(nums)
        farthest = 0  # 目前最大可到達的距離

        i = 0
        for i in range(n):
            # i + nums[i]
            # 在 i 的位置 + 可以走多少距離 = 最後的距離
            farthest = max(farthest, i + nums[i])

            # if farthest < i:
            # 停留在原地 無法前進
            if farthest <= i != n - 1:
                return False

        # 大於即可
        # return farthest == n - 1
        return farthest >= n - 1

    def canJump_v1_space(self, nums: List[int]) -> bool:
        size = len(nums)

        # 空間壓縮版本
        dp_0 = -1
        dp_1 = -1

        # base case
        prev = nums[0]

        for i in range(1, size):
            dp_0 = prev

            if dp_0 <= 0:
                break

            dp_1 = max(
                dp_0 - 1,  # 不停在此格
                nums[i]  # 停在此格
            )

            # 當執行最後一次的時候
            # 會造成 dp_0 == dp_1
            # 若解答需要 dp 倒數第二個 的資訊
            # 答案就會失敗
            #
            # dp_0 = dp_1

            # 利用一個暫存欄位
            # 保留前一個
            prev = dp_1

        return True if size == 1 else dp_0 > 0

    def canJump_v1(self, nums: List[int]) -> bool:
        size = len(nums)
        # 在第 i 個位置, 最多能走幾步
        dp = [0] * size

        # base case
        dp[0] = nums[0]

        for i in range(1, size):

            # 無法到達 i 就中斷程式
            if dp[i - 1] <= 0:
                break

            dp[i] = max(
                dp[i - 1] - 1,  # 不停在此格
                nums[i]  # 停在此格
            )

        # 只有一個元素的時候會錯誤
        # 不用走就可以到目的地
        # return dp[size - 2] > 0

        # 目的地的前一個 是否有足夠步伐
        return True if size == 1 else dp[size - 2] > 0


if __name__ == '__main__':
    # print(Solution().canJump_v1([3, 2, 1, 0, 4]))
    # print(Solution().canJump_v1([0, 2, 3]))
    print()

    print(Solution().canJump_v1_space([3, 2, 1, 0, 4]))
    print(Solution().canJump_v1_space([0, 2, 3]))
    print(Solution().canJump_v1_space([2, 0, 0]))
    print()

    print(Solution().canJump_greedy([3, 2, 1, 0, 4]))
    print(Solution().canJump_greedy([0, 2, 3]))
    print(Solution().canJump_greedy([2, 0, 0]))
