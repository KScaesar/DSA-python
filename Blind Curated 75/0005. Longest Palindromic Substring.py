class Solution:
    # https://leetcode.com/problems/longest-palindromic-substring/
    # 算法筆記 p384
    # https://leetcode.com/problems/longest-palindromic-substring/solutions/127837/longest-palindromic-substring/?orderBy=most_votes

    # 相似題 0647. Palindromic Substrings

    def longestPalindrome_dp(self, s: str) -> str:
        n = len(s)

        # dp 錯誤定義
        # 子字串中 s[i~j] 的最長子字串是什麼
        #
        # dp 正確定義
        # 子字串中 s[i~j] 是否為回文子字串
        dp = [[False] * n for _ in range(n)]

        # base case
        for k in range(n):
            # 奇數回文
            dp[k][k] = True

            # 偶數回文
            if k < n - 1 and s[k] == s[k + 1]:
                dp[k][k + 1] = True

        # 從下到上, 從左到右
        for i in range(n - 2, -1, -1):

            # 因為對角線是 base case
            # 所以直接跳過不考慮
            for j in range(i + 1, n):
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True

        # 一個字母本身就是迴文，所以先宣告參數
        max_len = 1
        start = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and j - i + 1 > max_len:
                    start = i
                    max_len = j - i + 1

        return s[start:start + max_len]

    def longestPalindrome(self, s: str) -> str:
        # 設一開始找到了最長的迴文總共是5個字，那之後就都以5個字的標準來找下一個迴就好

        max_len = 0
        start = -1

        # for i in range(len(s) - 1):
        #
        # 不需要特別限制結束終點在 len - 1
        # 不然無法處理 s 只有單一字符的情況
        # 越界處理, 已經在 get_palindrome 進行了
        for i in range(len(s)):
            odd_start, odd_len = self.get_palindrome(s, i, i)  # 期望以奇數長度獲得回文
            if odd_len > max_len:
                max_len = odd_len
                start = odd_start

            even_start, even_len = self.get_palindrome(s, i, i + 1)  # 期望以偶數長度獲得回文
            if even_len > max_len:
                max_len = even_len
                start = even_start

            # print(odd_start, odd_len)
            # print(s[start:start + max_len])

        return "" if max_len == 0 else s[start:start + max_len]

    def get_palindrome(self, s, left, right) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # sub string = s[l + 1:r], len = r - ( l + 1) = r - l - 1
        return left + 1, right - left - 1


if __name__ == '__main__':
    print(f'{Solution().longestPalindrome("babad")}')
    print(f'{Solution().longestPalindrome_dp("babad")}')
    print()
    print(f'{Solution().longestPalindrome("a")}')
    print(f'{Solution().longestPalindrome_dp("a")}')
    print()
    print(f'{Solution().longestPalindrome("cbbd")}')
    print(f'{Solution().longestPalindrome_dp("cbbd")}')
    print()
