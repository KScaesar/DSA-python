import collections


class Solution:
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/
    # slide window
    def lengthOfLongestSubstring_v2(self, s: str) -> int:
        # v2 是 v1 的簡化寫法
        # 尤其注意 更新資訊所放的位置
        # 是在收縮之後

        subset = collections.defaultdict(int)
        slow = fast = 0
        start = 0
        _len = 0
        while fast < len(s):
            c1 = s[fast]
            fast += 1
            subset[c1] += 1

            while subset[c1] > 1:
                c2 = s[slow]
                slow += 1
                subset[c2] -= 1

            # 更新資訊 寫法1
            if fast - slow > _len:
                start = slow
                _len = fast - slow

            # 更新資訊 寫法2
            # _len = max(_len, fast - slow)

        print(s[start:start + _len])
        return _len

    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = collections.defaultdict(int)
        char_duplicate = False

        # 设计为左闭右开区间
        # 因为这样初始化 left = right = 0 时区间 [0, 0) 中没有元素
        # https://labuladong.github.io/algo/2/20/27/
        slow = fast = 0

        start = 0
        _len = 0
        while fast < len(s):

            c1 = s[fast]
            fast += 1

            if charset[c1] == 0:
                charset[c1] = 1
            else:
                charset[c1] += 1
                char_duplicate = True

            # 更新資訊 寫法3
            if not char_duplicate and fast - slow > _len:
                start = slow
                _len = fast - slow

            while char_duplicate:

                # 收縮的流程, 先檢查再收縮
                c2 = s[slow]
                slow += 1

                if charset[c2] > 1:
                    char_duplicate = False
                charset[c2] -= 1

        print(s[start:start + _len])
        return _len


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring_v2("abcabcbb"))
    print(Solution().lengthOfLongestSubstring_v2("bbbb"))
    print(Solution().lengthOfLongestSubstring_v2("pwwkew"))
    print(Solution().lengthOfLongestSubstring_v2("b"))
    print(Solution().lengthOfLongestSubstring_v2(""))
    print(Solution().lengthOfLongestSubstring_v2("b2"))
