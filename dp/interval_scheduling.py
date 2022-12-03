import bisect


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
            line_start, line_end = intervals[i]
            if line_start >= end:
                end = line_end
            else:
                remove_count += 1

        return remove_count

    def job_scheduling_v2(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:

        # sort each list according to the start time
        # leetcode 範例 合成排序後, 再分解回原本數列
        # https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/739343/python-dp-82-time/
        #
        # startTime, endTime, profit = (list(x) for x in zip(*sorted(zip(startTime, endTime, profit))))

        # startTime, endTime, profit = list(zip(*sorted(zip(startTime, endTime, profit), key=lambda x: x[1])))
        # print(startTime, endTime, profit)

        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        # print(jobs)

        n = len(jobs)
        dp = [0] * n

        prev = []
        for i in range(n):
            start, end, money = jobs[i]

            # https://docs.python.org/3/library/bisect.html#searching-sorted-lists
            # get jobs[i].start >= job[prev].end
            # 在 jobs.end 找出 小於等於 start 的 索引
            # python 3.10 才有 key 這個參數, 所以在 leetcode 無法使用這個語法
            prev_job = bisect.bisect_right(jobs, (start,), key=lambda x: (x[1],)) - 1
            prev.append(prev_job)
            if prev_job >= 0:
                dp[i] = max(dp[i - 1], dp[prev_job] + money)
            else:
                dp[i] = max(dp[i - 1], money)
            # print(dp[i])

        # print(prev)
        return dp[-1]

    def job_scheduling_v1(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # leetcode 1235
        # https://leetcode.com/problems/maximum-profit-in-job-scheduling/
        # https://youtu.be/YMdnGChsvvo?t=892
        # https://www.geeksforgeeks.org/weighted-job-scheduling/

        # 依照 end time 進行 sort
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        # print(jobs)

        # -1 表示找不到 前一個可執行的工作
        # 比如說 執行第0個工作 不可能有前一個
        prev = [-1] * n

        # 可以利用 bisect 找出目標值
        for i in range(n - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if jobs[i][0] >= jobs[j][1]:
                    prev[i] = j
                    break

        # print(jobs, prev)

        dp = [0] * n
        for i in range(0, n):
            prev_job = prev[i]
            if prev_job >= 0:
                dp[i] = max(dp[i - 1], dp[prev_job] + jobs[i][2])
            else:
                dp[i] = max(dp[i - 1], jobs[i][2])
            # print(dp[i])

        return dp[- 1]


if __name__ == '__main__':
    obj = Solution()
    print(f'erase_overlap_intervals = {obj.erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])}')
    print()
    print(f'job_scheduling_v1 expect=120, actual={obj.job_scheduling_v1([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70])}')
    print(f'job_scheduling_v2 expect=120, actual={obj.job_scheduling_v2([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70])}')
    print()
    print(f'job_scheduling_v1 expect=150, actual={obj.job_scheduling_v1([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60])}')
    print(f'job_scheduling_v2 expect=150, actual={obj.job_scheduling_v2([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60])}')
