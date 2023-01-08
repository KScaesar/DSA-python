import tool


class Solution:
    # https://leetcode.com/problems/longest-repeating-character-replacement/

    # https://github.com/halfrost/LeetCode-Go/tree/master/leetcode/0424.Longest-Repeating-Character-Replacement
    # https://github.com/aQuaYi/LeetCode-in-Go/blob/master/Algorithms/0424.longest-repeating-character-replacement/longest-repeating-character-replacement.go

    # 不是 dp 類型的題目, 而是 sliding window

    # 下次複習 要多注意這題

    def characterReplacement(self, s: str, k: int) -> int:
        # 完全沒想法, 不知道怎麼寫
        # 想不出來, 擴展要檢查什麼條件, 收縮要檢查什麼條件

        # 算法筆記 p92 四個步驟
        # 我想不到 第四點 ans 要在哪邊更新

        window = dict()
        max_count = 0

        left = 0
        right = 0
        size = len(s)
        ans = 0

        while right < size:
            c1 = s[right]
            right += 1

            window[c1] = window.get(c1, 0) + 1
            max_count = max(max_count, window[c1])
            # ans = max(ans, right - left) # 錯誤的更新位置

            # 此時 right 已經到下一個
            #
            # (right - left) - max_count == k 的含义是
            # 在 s[left:right) 中有 max_count 个相同的字母 X 和 k 个不同于 X 的字母
            # 通过 k 次修改后，範圍內就全是 X 了
            #
            #  (right - left) - max > k  的含义是
            # 无法通过 k 次修改，把範圍中的字母全部变成 X
            # 只好把 window left+=1
            while (right - left) - max_count > k:
                c2 = s[left]
                left += 1

                window[c2] -= 1
            ans = max(ans, right - left)  # 正確的更新位置

        return ans

    def characterReplacement_fail(self, s: str, K: int) -> int:
        # 困難點, 不知道怎麼說明 k 的定義, 才能符合遞歸推導

        # dp[k][i], 0~i 個字符, 可以修改 k 次, 最長相同字串的長度
        # 以 i 為起點, 至少會重複自己, 所以長度為 1
        #
        dp = [[1] * len(s) for _ in range(K + 1)]

        for i in range(len(s)):
            if s[i] == s[i - 1]:
                dp[0][i] += dp[0][i - 1]

        for k in range(1, K + 1):
            for i in range(1, len(s)):
                dp[k][i] = max(
                    dp[k - 1][i - 1] + 1,
                    dp[k][i - 1]
                )

        tool.print_matrix(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().characterReplacement("ABAB", 2))
    # print(Solution().characterReplacement("AAAB", 2))
