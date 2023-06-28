class Solution:
    # https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

    # https://hackmd.io/X-jeuBQaR7amGQfALM2XDQ?view#Sliding-Window-vs-%E9%9B%99%E6%8C%87%E9%87%9D

    # https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2948183/python-clean-12-line-sliding-window-solution-with-explanation/

    # https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2947980/c-two-pointer-solution-o-n/

    def takeCharacters(self, s: str, k: int) -> int:
        # 把問題轉換成 take at most count(c) - k of each character from middle.
        # finding the longest substring where the occurrence of each character is within limits

        window = {c: 0 for c in 'abc'}
        target = {c: v for c, v in window.items()}
        for c in s:
            target[c] += 1

        target = {c: v - k for c, v in target.items()}
        for v in target.values():
            if v < 0:
                return -1
        # print(f'window={window}')
        # print(f'target={target}')

        longest_substring_len = 0
        size = len(s)
        l, r = 0, 0

        while r < size:
            c1 = s[r]
            window[c1] += 1
            r += 1

            while window[c1] > target[c1]:
                # 更新資訊 不應該在這邊
                # longest_substring_len = r - l

                c2 = s[l]
                window[c2] -= 1
                l += 1

            # 更新資訊 正確的位置
            longest_substring_len = max(r - l, longest_substring_len)

        # print(f'size={size} longest_substring_len={longest_substring_len}')
        return size - longest_substring_len


if __name__ == '__main__':
    print(Solution().takeCharacters('aabaaaacaabc', 2))
