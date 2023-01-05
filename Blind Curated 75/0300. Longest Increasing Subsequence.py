from typing import List


class Solution:
    # https://leetcode.com/problems/longest-increasing-subsequence/

    # https://labuladong.github.io/algo/di-er-zhan-a01c6/zi-xu-lie--6bc09/dong-tai-g-4ef47/
    # https://github.com/halfrost/LeetCode-Go/tree/master/leetcode/0300.Longest-Increasing-Subsequence
    # https://ithelp.ithome.com.tw/articles/10253577

    def lengthOfLIS(self, nums: List[int]) -> int:
        # 以前的 testcase 不會 timeout
        # 現在要求時間複雜度 nlogN 才可以ac
        # 因此本題 O(n^2) 無法通過

        # O(n^2)
        # 算法筆記 p99
        #
        # 自己想不到 如何推導出狀態轉移函數
        # 思考卡在做選擇
        # 不知道如何進行歸納法 根據上次的值 得到這次的值

        size = len(nums)
        # 以num[i]結尾的最長遞增子序列長度
        # i之前包括i的以nums[i]结尾的最长递增子序列的长度
        # dp = [0] * size # 初始狀態直接用 1, 因為定義了要包含自己, 所以至少長度為 1
        dp = [1] * size

        # 錯誤的迭代過程
        # 例如 nums = [0,1,0,3,2,3]
        # 當 i = 3, 只能找到 j = 2
        # 更好的選擇是 j = 1
        #
        # for i in range(size):
        #     j = i - 1
        #     while 0 <= j and nums[j] >= nums[i]:
        #         j -= 1
        #     if nums[j] < nums[i]:
        #         dp[i] += dp[j]

        for i in range(size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
