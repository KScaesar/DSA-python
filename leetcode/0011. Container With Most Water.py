from typing import List


class Solution:
    # https://leetcode.com/problems/container-with-most-water/
    # two pointer
    #
    # 算法筆記 p374
    # https://labuladong.github.io/algo/4/33/128/
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        lo = 0
        hi = n - 1
        ans = 0

        while lo <= hi:
            lo_h = height[lo]
            hi_h = height[hi]
            size = min(lo_h, hi_h) * (hi - lo)
            ans = max(size, ans)
            # print(f'lo=>{lo}:{lo_h}, hi=>{hi}:{hi_h}')

            if lo_h > hi_h:
                hi -= 1
            else:
                lo += 1

        return ans


if __name__ == '__main__':
    print(f'{Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])}')
