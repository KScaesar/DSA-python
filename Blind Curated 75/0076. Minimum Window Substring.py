import collections


class Solution:
    # https://leetcode.com/problems/minimum-window-substring/
    def minWindow(self, s: str, t: str) -> str:

        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        need_keys = list(need.keys())
        need_keys_count = len(need_keys)

        window = collections.defaultdict(int)
        window_keys_count = 0

        size = len(s)
        slow = 0
        fast = 0
        sub_len = size + 1
        sub_start = -1

        while fast < size:
            fast_key = s[fast]
            fast += 1

            if fast_key not in need_keys:
                continue

            window[fast_key] += 1
            if window[fast_key] == need[fast_key]:
                window_keys_count += 1

            while window_keys_count == need_keys_count:

                # 注意: [left, right]閉區間 長度是 right - left + 1
                # 但 這邊的 fast 已經是下一個, 所以不用 + 1
                if fast - slow < sub_len:
                    sub_len = fast - slow
                    sub_start = slow

                slow_key = s[slow]
                slow += 1

                if slow_key not in need_keys:
                    continue

                window[slow_key] -= 1
                if window[slow_key] < need[slow_key]:
                    window_keys_count -= 1

        return s[sub_start:sub_start + sub_len] if sub_len <= size else ""


if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
    print(Solution().minWindow("a", "aa"))
    print(Solution().minWindow("aa", "aa"))
