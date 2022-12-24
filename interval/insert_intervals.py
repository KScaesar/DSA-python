import bisect


class Solution:
    # leetcode 57
    # https://leetcode.com/problems/insert-interval/
    # https://blog.techbridge.cc/2020/01/16/leetcode-%E5%88%B7%E9%A1%8C-pattern-merge-intervals/
    #
    # 暴力法
    # 先把 new 加入 array
    # 重新 sort
    # 再仿造 leetcode 56(merge interval) 的作法

    # 超優雅版本 v4
    # 就學這個吧

    # 本題得到的教訓
    # 用 binary search 找 >= , <= 要考慮的東西很多
    # 未必比較好寫
    # 乖乖用 for range 比較不影響思考

    def insert_v1_fail(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # 失敗原因
        # 沒有考慮到 new 跨 多個線段的情境

        if len(intervals) == 0:
            return []

        n = len(intervals)

        # 在數列中, 找出 小於等於 new 的 index
        # 也就是 leetcode 56(merge interval) 中 的前一個線段
        #
        # 後來發現, 以下是錯誤想法, 被 56題的思想綁住
        # 只想著依照 start的排序 來找前一個
        # 應該使用其他條件, 詳情看 v2
        prev_idx = bisect.bisect_right(intervals, newInterval) - 1

        if prev_idx == -1:  # prev_idx 不存在, 由 new 當 prev
            prev = newInterval
            current = intervals[0]

            if current[0] > prev[1]:  # current_start > prev_end
                intervals.insert(0, prev)
                return intervals
            else:
                data = [prev[0], max(prev[1], current[1])]
                intervals[0] = data
                return intervals
        else:
            pass
            # 此處邏輯很亂, 可以參考, 不要深入
            # while True:
            #     prev = intervals[prev_idx]
            #     current = newInterval
            #     if current[0] > prev[1]:  # current_start > prev_end
            #         prev_idx += 1
            #     else:
            #         data = [prev[0], max(prev[1], current[1])]
            #         intervals[prev_idx] = data
            #         return intervals

    def insert_v2(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # 此題 自己想的 條件太多
        # 無法清楚思考
        # 到底要考慮哪些邊界
        # 看看其他人的解法吧 v3

        n = len(intervals)
        if n == 0:
            # return [] 不要忘了, 此題目是 insert
            return [newInterval]

        # 極端情況 new 完全覆蓋 intervals
        if newInterval[0] < intervals[0][0] and newInterval[1] > intervals[-1][1]:
            return [newInterval]

        # 先處理 new 插入在極端情況
        # head
        idx = bisect.bisect_right(intervals, [newInterval[0]], key=lambda x: [x[0]]) - 1
        if idx == -1:
            if intervals[0][0] > newInterval[1]:
                intervals.insert(0, newInterval)
                return intervals
            else:
                data = [newInterval[0], max(newInterval[1], intervals[0][1])]
                intervals[0] = data
                return intervals
        else:
            if intervals[idx][1] < newInterval[0]:
                intervals.insert(idx + 1, newInterval)
                n += 1  # 要記得更新
            else:
                intervals[idx] = [intervals[idx][0], max(intervals[idx][1], newInterval[1])]

            # 從插入的地方, 重新執行 merge interval
            result = [x for x in intervals[:idx + 1]]
            for i in range(idx + 1, n):  # insert 後, n 會多一個, 前面要更新 n
                prev = result[-1]
                current = intervals[i]
                if prev[1] < current[0]:
                    result.append(current)
                else:
                    result[-1][1] = max(current[1], prev[1])

            return result

        # tail
        # idx = bisect.bisect_left(intervals, [newInterval[1]], key=lambda x: [x[1]])
        # if idx == n:
        #     if intervals[-1][1] < newInterval[0]:
        #         intervals.append(newInterval)
        #         return intervals
        #     else:
        #         data = [min(intervals[-1][0], newInterval[0]), newInterval[1]]
        #         intervals[-1] = data
        #         return intervals

    def insert_v3(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # https://blog.techbridge.cc/2020/01/16/leetcode-%E5%88%B7%E9%A1%8C-pattern-merge-intervals/

        n = len(intervals)
        result = []

        # 在 intervals end 找出 小於 new start 的 索引
        idx = bisect.bisect_left(intervals, [newInterval[0]], key=lambda x: [x[1]]) - 1
        if idx == - 1:
            idx = 0  # 沒發現的話, 從頭來過

            # 以下是錯誤作法
            # intervals.append(newInterval)
            # return intervals
        else:
            # 絕對不可能和 new 有接觸的線段
            # 先放入 result
            # 千萬記得 +1 前進到 下一步
            idx += 1
            result = [x for x in intervals[:idx]]

        # 後續  idx線段 和 new 有 六種情境
        # 提示性質, 與此題解法, 不相關

        # overlaps 的計算, 有點玄
        # 個人感覺不好理解
        while idx < n and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0], newInterval[0])
            newInterval[1] = max(intervals[idx][1], newInterval[1])
            idx += 1
        result.append(newInterval)

        for i in range(idx, n):
            result.append(intervals[i])

        return result

    def insert_v4(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # Blind Curated 75 目錄有不同作法, 可以互相參考

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # overlaps 的計算, 有點玄
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res


if __name__ == '__main__':
    obj = Solution()

    # sol1 = obj.insert_v1_fail([[1, 3], [6, 9]], [2, 5])
    # print(f'insert_v1_fail: expect=[[1,5],[6,9]], actual={sol1}')
    #
    # sol2 = obj.insert_v1_fail([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    # print(f'insert_v1_fail: expect=[[1,2],[3,10],[12,16]], actual={sol2}')

    sol3 = obj.insert_v2([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    print(f'insert_v2: expect=[[1,2],[3,10],[12,16]], actual={sol3}')

    sol4 = obj.insert_v2([[0, 7], [8, 8], [9, 11]], [4, 13])
    print(f'insert_v2: expect=[[0,13]], actual={sol4}')

    sol5 = obj.insert_v2([[1, 5]], [6, 8])
    print(f'insert_v2: expect=[[1,5],[6,8]], actual={sol5}')

    sol6 = obj.insert_v2([[1, 5], [6, 8]], [0, 9])
    print(f'insert_v2: expect=[[0,9]], actual={sol6}')
