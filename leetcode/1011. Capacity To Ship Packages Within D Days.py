from typing import List


class Solution:
    # https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
    # Binary Search Problems
    # 算法筆記 p369
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        w_max = sum(weights)
        w_min = max(weights)

        while w_min <= w_max:
            mid = w_min + (w_max - w_min) // 2
            need_day = self.finsih_day(weights, mid)
            # print(w_max, w_min, mid)
            # print(need_day, days)
            # print()
            if need_day == days:
                # 重點
                # 即使滿足天數
                # 還是要嘗試看看 有沒有更小重量的可能
                # 所以不能直接回傳
                # 作法類似 left_bound binary search
                #
                # return mid
                w_max = mid - 1
            elif need_day < days:
                # w_min = mid + 1
                w_max = mid - 1  # 搞清楚 載重 和 天數的關係, 載重低 天數多
            elif need_day > days:
                # w_max = mid - 1
                w_min = mid + 1

        return w_min

    def finsih_day(self, weights, w_max) -> int:
        day = 1
        w_cap = 0
        for w in weights:
            w_cap += w
            if w_cap > w_max:
                day += 1
                w_cap = w
        return day


if __name__ == '__main__':
    print(f'{Solution().shipWithinDays([1, 2, 3, 1, 1], 4)}')
