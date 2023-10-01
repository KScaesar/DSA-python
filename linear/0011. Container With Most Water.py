from typing import List


# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            height_l = height[l]
            height_r = height[r]
            area = min(height_l, height_r) * (r - l)
            ans = max(area, ans)
            if height_l > height_r:
                r -= 1
            else:
                l += 1
        return ans


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
