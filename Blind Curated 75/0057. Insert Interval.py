import bisect
from typing import List


class Solution:
    # https://leetcode.com/problems/insert-interval/description/

    def insert_v2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        merge = newInterval.copy()
        ans = []

        if size == 0:
            ans.append(merge)
            return ans

        i = 0
        # while  intervals[i][1] < newInterval[0]: # 執行到最後一個元素, 會出現 index of range
        while i < size and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < size and not newInterval[1] < intervals[i][0]:
            merge[0] = min(merge[0], intervals[i][0])
            merge[1] = max(merge[1], intervals[i][1])
            i += 1
        ans.append(merge)

        while i < size:
            ans.append(intervals[i])
            i += 1

        return ans

    def insert_v2_fail(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 超簡潔寫法
        # https://leetcode.com/problems/insert-interval/solutions/21602/short-and-straight-forward-java-solution/
        #
        # https://leetcode.com/problems/insert-interval/solutions/21622/7-lines-3-easy-solutions/

        # 太多錯誤, 沒辦法添加更多註解
        # 重寫函數

        size = len(intervals)
        # 此實作需要注意長度
        if size == 0:
            return [newInterval]

        ans = []
        i = 0

        # 前段 未重合區段
        while i < size:
            line = intervals[i]
            if line[1] < newInterval[0]:
                ans.append(line)
                i += 1
            else:
                break

        # 中間 重合區端
        merge = [float('inf'), float('-inf')]  # 失敗原因 可能把 初始 merge 送到 ans 的情況, 也就是結果出現無限大的情況
        while i < size:
            line = intervals[i]
            # i += 1  # 錯誤位置

            # 前後區段的反向條件
            # 搞清楚是 or 還是 and 條件
            #
            # 最後發現 不是 or 也不是 and
            # if line[1] >= newInterval[0] or newInterval[1] >= line[0]:
            #     merge[0] = min(merge[0], line[0], newInterval[0])
            #     merge[1] = max(line[1], newInterval[1])
            #     i += 1

            if newInterval[1] < line[0]:
                # ans.append(merge) # 插入應該放在迴圈外面,不然可能發生最後一個元素比較後, 沒進行插入
                break
            merge[0] = min(merge[0], line[0], newInterval[0])
            merge[1] = max(line[1], newInterval[1])
            i += 1  # i 的程式碼位置放錯, 會造成少插入元素

        ans.append(merge)

        # 後段 未重合區段
        while i < size:
            line = intervals[i]
            ans.append(line)
            i += 1

        return ans

    def insert_v1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # interval 目錄有不同作法, 可以互相參考

        # 本作法是先找出插入點
        # 進行類似 merge 的合併操作

        size = len(intervals)
        ans = []

        start_index = bisect.bisect_right([x[0] for x in intervals], newInterval[0]) - 1
        if start_index == -1:
            ans.append(newInterval)
            for i in range(size):
                if ans[-1][1] < intervals[i][0]:
                    ans.append(intervals[i])
                else:
                    ans[-1][1] = max(ans[-1][1], intervals[i][1])

        else:
            for i in range(size):
                if i < start_index:
                    ans.append(intervals[i])
                elif i == start_index:

                    # 同樣也有三種情況要處理
                    if intervals[i][1] < newInterval[0]:
                        ans.append(intervals[i])
                        ans.append(newInterval)
                    else:
                        ans.append([intervals[i][0], max(intervals[i][1], newInterval[1])])

                else:
                    if ans[-1][1] < intervals[i][0]:
                        ans.append(intervals[i])
                    else:
                        ans[-1][1] = max(ans[-1][1], intervals[i][1])

        return ans


if __name__ == '__main__':
    print(Solution().insert_v1([[1, 3], [6, 9]], [2, 5]))
    print(Solution().insert_v1([[1, 5]], [6, 8]))
    print()

    print(Solution().insert_v2([[1, 3], [6, 9]], [2, 5]))
    print(Solution().insert_v2([[1, 5]], [6, 8]))
    print(Solution().insert_v2([[1, 5]], [2, 3]))
