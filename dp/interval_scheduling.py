class Solution:
    def erase_overlap_intervals(self, intervals: list[list[int]]) -> int:
        # leetcode 435
        # https://leetcode.com/problems/non-overlapping-intervals/
        # 算法筆記 p394 区间调度

        # intervals = sorted(intervals, key=lambda x: x[1])
        intervals.sort(key=lambda x: x[1])
        # print(intervals)

        n = len(intervals)
        remove_count = 0
        end = intervals[0][1]

        for i in range(1, n):
            line_start = intervals[i][0]
            line_end = intervals[i][1]
            if line_start >= end:
                end = line_end
            else:
                remove_count += 1

        return remove_count

    def job_scheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # leetcode 1235
        # https://leetcode.com/problems/maximum-profit-in-job-scheduling/
        # https://www.youtube.com/watch?v=YMdnGChsvvo
        # https://www.geeksforgeeks.org/weighted-job-scheduling/
        pass


if __name__ == '__main__':
    obj = Solution()
    print(f'erase_overlap_intervals = {obj.erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])}')
    pass
