import math
from typing import List


class Solution:
    # https://leetcode.com/problems/koko-eating-bananas/

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 算法筆記 p369

        # left, right = 1, sum(piles) # 不要搞錯 最大速度是什麼組成的
        left, right = 1, max(piles)
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2

            # 速度數列是遞增, 時間花費數列遞減
            # 目標是 花費時間
            # 所以應該在遞減數列找目標值
            #
            # 速度的下限值, 同等 花費時間的上限值
            if self.spend_time_v2(piles, mid) <= h:  # [mid,right] 以遞減數列來看待搜尋範圍
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def spend_time_v2(self, piles, speed) -> int:
        hours = 0
        for v in piles:
            # 寫法1
            hours += math.ceil(v / speed)

            # 寫法2
            # q = v // speed
            # r = v % speed
            # if r == 0:
            #     hours += q
            # else:
            #     hours += (q + 1)
        return hours

    def spend_time_v1(self, piles, speed) -> int:
        # 本題要求, 每小時只吃同一串香蕉
        # 此解法會出現 每小時吃兩串的情況
        # 和需求不同

        # 只是題外話, 跟此題目無關
        # v1的解法, 依據吃香蕉順序的不同, 還會產生不同的花費時間
        # 根據需求, 可能需要對 piles 進行 sort, 才可以求最佳值

        hours = 0
        remainder = 0
        for v in piles:
            if v + remainder <= speed:
                remainder = 0
            else:
                remainder = v + remainder - speed
            hours += 1

        if remainder == 0:
            return hours
        else:
            q = remainder // speed
            r = remainder % speed
            return hours + q if r == 0 else hours + q + 1


if __name__ == '__main__':
    # print(Solution().spend_time([4, 4, 10], 3))
    # print(Solution().minEatingSpeed([3, 6, 7, 11], 8))

    speed = 20
    print(Solution().spend_time_v1([30, 11, 23, 4, 20], speed))
    print(Solution().spend_time_v2([30, 11, 23, 4, 20], speed))
    print()

    print(Solution().spend_time_v1([20, 11, 23, 4, 30], speed))
    print(Solution().spend_time_v2([20, 11, 23, 4, 30], speed))
    print()

    print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))

    # print(math.ceil(10 / 2))
    # print(math.ceil(10 / 3))
