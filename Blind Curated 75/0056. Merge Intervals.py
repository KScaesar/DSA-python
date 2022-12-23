from typing import List


class Solution:
    # https://leetcode.com/problems/merge-intervals/

    # graph 連通分量解法
    # https://leetcode.com/problems/merge-intervals/solutions/127480/merge-intervals/?orderBy=most_votes

    def merge_v2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)

        ans = [intervals[0]]

        for i in range(1, size):
            # ans[-1][1] 等效 intervals[i-1][1]
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])

        return ans
        pass

    def merge_v1(self, intervals: List[List[int]]) -> List[List[int]]:
        # 困難點
        # 比如說 原本 3個 元素, merge 後變成 2個
        # 不知道如何 merge 成 新的陣列

        intervals.sort(key=lambda x: x[0])
        size = len(intervals)

        ans = [intervals[0]]

        for i in range(1, size):
            # ans[-1][1] 等效 intervals[i-1][1]
            if ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])

            # 重點 要注意 i.start 重合 i-1.end
            # elif intervals[i][0] < ans[-1][1] < intervals[i][1]:
            elif intervals[i][0] <= ans[-1][1] < intervals[i][1]:
                ans[-1][1] = intervals[i][1]
            elif intervals[i][1] <= ans[-1][1]:
                pass

        return ans


if __name__ == '__main__':
    print(Solution().merge_v1([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(Solution().merge_v1([[1, 4], [4, 5]]))
    print()

    print(Solution().merge_v2([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(Solution().merge_v2([[1, 4], [4, 5]]))
