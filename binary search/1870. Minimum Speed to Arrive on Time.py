import math
from typing import List


class Solution:
    # https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        l = 1
        # r = max(dist)
        r = 10e5  # 應該用題目給的最大值, 而不是數列中的最大值

        ans = -1
        while l <= r:
            mid = l + (r - l) // 2

            # 常常想不明白, 到底 ans 要放在 <= or >
            # 要仔細想想
            if self.costTime(dist, mid) <= hour:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    def costTime(self, dist, speed):
        total = 0
        last_idx = len(dist) - 1
        for i, d in enumerate(dist):
            if i == last_idx:
                total += d / speed
            else:
                total += math.ceil(d / speed)
            # print(total)
        return total


if __name__ == '__main__':
    print(Solution().minSpeedOnTime([1, 3, 2], 6))
    print()
    print(Solution().minSpeedOnTime([1, 3, 2], 2.7))
    print()
    print(Solution().minSpeedOnTime([1, 1, 100000], 2.1), f'expect=100000')

    # print(math.floor(1 / 2))
