class Solution:
    # https://leetcode.com/problems/palindromic-substrings/

    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.md

    # 相似題 0005. Longest Palindromic Substring

    def countSubstrings(self, s: str) -> int:
        def count_palindromic_by_center_expand(s, left, right) -> int:
            cnt = 0
            while 0 <= left and right < size and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt

        size = len(s)
        ans = 0

        for i in range(size):
            # odd len palindromic
            ans += count_palindromic_by_center_expand(s, i, i)

            # even len palindromic
            ans += count_palindromic_by_center_expand(s, i, i + 1)

        return ans


if __name__ == '__main__':
    print(Solution().countSubstrings("abc"))
