from typing import List


class Solution:
    # https://leetcode.com/problems/maximum-subarray/

    def maxSubArray(self, nums: List[int]) -> int:
        # 算法筆記 p111

        size = len(nums)

        # dp[i] 以下兩種定義, 是不同意思
        # 1.以num[i] 結尾的最大子陣列總和
        # 2.nums[0~i] 最大子陣列的總和
        dp = [0] * size

        # base case
        dp[0] = nums[0]

        ans = nums[0]

        for i in range(1, size):
            dp[i] = max(
                dp[i - 1] + nums[i],  # 和之前的字串連接
                nums[i]  # 自己開啟一個子字串
            )
            ans = max(ans, dp[i])

        return ans

    def maxSubArray_compression_state_v2(self, nums: List[int]) -> int:
        # 算法筆記 p160
        # 空間壓縮就是投影
        # 1D to constant

        size = len(nums)
        dp0 = None
        dp1 = 0
        ans = nums[0]

        for i in range(size):
            for j in range(i, size):
                if i != j:
                    dp1 = dp0 + nums[j]
                elif i == j:
                    dp1 = nums[j]

                dp0 = dp1  # 所有選擇路徑執行後, 才開始紀錄前一個數值
                ans = max(ans, dp1)

        # print(dp)
        return ans

    def maxSubArray_compression_state_v1(self, nums: List[int]) -> int:
        # 算法筆記 p160
        # 空間壓縮就是投影
        # 2D to 1D

        size = len(nums)
        dp = [0] * size
        ans = nums[0]

        for i in range(size):
            for j in range(i, size):
                if i != j:
                    dp[j] = dp[j - 1] + nums[j]
                elif i == j:
                    dp[j] = nums[j]
                ans = max(ans, dp[j])

        # print(dp)
        return ans

    def maxSubArray_timeout(self, nums: List[int]) -> int:
        size = len(nums)

        # dp[i][j] i~j 的總和是多少
        dp = [[0] * size for _ in range(size)]

        ans = nums[0]

        # base case
        for k in range(size):
            dp[k][k] = nums[k]

        # 這是一個上三角走訪
        for i in range(size):
            # 一定要走訪到對角線
            # 不然會漏掉一些情況沒進行比較
            # for j in range(i + 1, size):
            for j in range(i, size):
                if i != j:
                    dp[i][j] = dp[i][j - 1] + nums[j]
                ans = max(ans, dp[i][j])

        print(dp)
        return ans


if __name__ == '__main__':
    # print(Solution().maxSubArray_timeout([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(Solution().maxSubArray_timeout([-2, 1]))

    # print(Solution().maxSubArray_compression_state_v1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(Solution().maxSubArray_compression_state_v1([-2, 1]))

    print(Solution().maxSubArray_compression_state_v2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray_compression_state_v2([-2, 1]))

    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray([-2, 1]))
