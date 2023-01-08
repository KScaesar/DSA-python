from typing import List


class Solution:
    # https://leetcode.com/problems/non-overlapping-intervals/

    # 不確定是 merge interval 還是 greedy interval schedule

    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.md

    # 需要多練習不重疊區間的解法, 每次都忘
    # https://hackmd.io/@linzong/BJMrws1ZK
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 應該是 greedy
        # 先求出最多有幾個區間不會重疊
        # 再用 總數量 - 不重疊區間
        #
        # 看圖比較容易想出來怎麼寫
        # 不然常常忘記實做方法

        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                cnt += 1
                end = intervals[i][1]
        return len(intervals) - cnt


if __name__ == '__main__':
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
