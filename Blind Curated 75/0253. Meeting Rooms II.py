import heapq


class Solution(object):

    # https://ithelp.ithome.com.tw/articles/10298593
    # https://labuladong.github.io/algo/di-er-zhan-a01c6/tan-xin-le-9bedf/sao-miao-x-af1fb/
    # https://www.lintcode.com/problem/919/

    # 給予多個會議時間的區段
    # 求最少要幾個 會議室 才能讓所有會議準時開會
    # 換而言之, 同一個時間點, 求重疊區間最多有幾個

    # 另一種問法是 求最多有幾個不重疊區間
    # 這樣的問法才是利用 end 進行排序, 進行 greedy 策略

    # 此題目的實做重點是
    # 如何讓多個區間
    # 依照時間順序 輸出 start end

    def minMeetingRooms_v2(self, intervals: list[list[int]]) -> int:
        # 將區段進行投影
        # 但用 heap 進行排序

        start_heap = []
        end_heap = []
        size = len(intervals)
        for i in range(size):
            heapq.heappush(start_heap, intervals[i][0])
            heapq.heappush(end_heap, intervals[i][1])

        ans = 0
        count = 0
        while len(start_heap) != 0:
            start = start_heap[0]
            end = end_heap[0]
            if start < end:
                print(start, "", end='')
                heapq.heappop(start_heap)
                count += 1
            else:
                print(end, "", end='')
                heapq.heappop(end_heap)
                count -= 1
            ans = max(ans, count)

        # 對於此題, 是不必要的
        # 只是想練習, 輸出剩餘的元素
        # 該怎麼作
        while len(end_heap) != 0:
            print(heapq.heappop(end_heap), "", end='')

        print()
        return ans

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # 將區段進行投影

        size = len(intervals)
        start = sorted(line[0] for line in intervals)
        end = sorted(line[1] for line in intervals)

        ans = 0
        count = 0

        i = 0
        j = 0

        # 這個迭代的寫法
        # 我自己想不到
        while i < size:  # 當 pStart 走到 n-1 就可以拿到最大值 因為代表不會再有會議需要開始
            if start[i] < end[j]:
                i += 1
                count += 1
            else:  # 相等的情況, 不需要開啟新的會議室, 而是關閉
                j += 1
                count -= 1
            ans = max(ans, count)

        return ans

    def minMeetingRooms_fail(self, intervals: list[list[int]]) -> int:
        # 失敗原因
        # 只能判斷局部區域是否重疊
        # 無法找出 整體最多重疊幾個區端
        #
        # Merge Intervals 的題目中
        # 討論了 兩個 interval 之間會有 6種關係
        # 使用 start 進行排序後, 可以簡化為 3種關係
        #
        # 判斷是否重疊的條件是
        # if intervals[i - 1].end < intervals[i].start
        # then 兩個區段不重疊

        size = len(intervals)
        intervals.sort(key=lambda x: x[0])
        ans = 0
        for i in range(size):
            if i == 0:
                ans += 1
                continue
            if intervals[i - 1][1] > intervals[i][0]:
                ans += 1

        return ans


if __name__ == '__main__':
    # print(Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]))
    print(Solution().minMeetingRooms_v2([[0, 30], [5, 10], [15, 20]]))
