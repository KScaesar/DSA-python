class Solution(object):
    # https://github.com/apachecn/apachecn-algo-zh/blob/master/docs/leetcode/python/252._Meeting_Rooms.md
    # https://ithelp.ithome.com.tw/articles/10298588
    def canAttendMeetings(self, intervals: list[list[int]]):

        # 重點注意, 要比較 interval 的各種關係
        # 通常都是排序 line start
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            if i == 0:
                continue

            # 相等的情況是可以參加會議的
            # merge interval, 相等的時候, 算重疊
            # 但會議 相等的時候, 不算重疊
            # if intervals[i - 1][1] >= intervals[i][0]:
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
