import bisect
import queue


class Solution:
    # 436. Find Right Interval
    # https://leetcode.com/problems/find-right-interval/
    def findRightInterval_v1(self, intervals: list[list[int]]) -> list[int]:

        # 遇到 intervals 長度極大時
        # leetcode 會出現 time limit
        # 整體邏輯是對的
        # 但 O(n) = n^2 太差
        # 應該可以用 binary search 改進, 請看 v3

        memo = {tuple(line): index for index, line in enumerate(intervals)}
        intervals.sort()
        n = len(intervals)
        ans = [-1] * n  # 預設不存在 右側區間
        print(intervals)

        for i in range(n - 1):
            left_line = tuple(intervals[i])

            # 因為題目沒有限制 right 只能存在 i+1 的位置
            # right 可以存在 i+n 的位置
            # 所以要加上第二層迴圈
            for j in range(i + 1, n):
                right_line = tuple(intervals[j])

                # 可能出現 某個線段 start 極小, end 極大
                # ex intervals = [[1,4],[2,3],[3,4]]
                if right_line[0] >= left_line[1]:
                    ans[memo[left_line]] = memo[right_line]
                    break

        return ans

    def findRightInterval_v3(self, intervals: list[list[int]]) -> list[int]:
        # 可通過 leetcode 測驗
        # 不會 time limit

        memo = {tuple(line): index for index, line in enumerate(intervals)}
        intervals.sort()
        n = len(intervals)
        ans = [0] * n  # 預設不存在 右側區間
        # print(intervals)

        for i in range(n):
            left_line = tuple(intervals[i])

            # 在 intervals 的 start 中, 找了一個 大於等於 end 的索引
            target_idx = bisect.bisect_left(intervals, [left_line[1]], key=lambda x: [x[0]])
            if target_idx == n:
                ans[memo[left_line]] = -1
            else:
                right_line = tuple(intervals[target_idx])
                ans[memo[left_line]] = memo[right_line]

        return ans

    def findRightInterval_v2_fail(self, intervals: list[list[int]]) -> list[int]:
        # https://blog.techbridge.cc/2020/03/15/leetcode-%E5%88%B7%E9%A1%8C-pattern-two-heaps/
        # 這題的 Two Heaps 解法寫起來又臭又長，leetcode discussion 上有其他簡潔有效率的解法 (二叉搜索)

        # 对每个 interval 我只关心它的右边界，和剩余所有 interval 的左边界。
        # 如果它的右边界确定的时候，要找所有比它小的左边界

        # 個人看法, 用 two heap 的作法, 超難理解
        # 要了解 two heap, 還是參考其他題目吧
        # https://www.youtube.com/watch?v=zBuTgoUjynY

        # 此題 two heap 類似雙指針的概念
        # https://youtu.be/wh2lT04u_cg?t=265

        n = len(intervals)

        start_max_heap = queue.PriorityQueue(n)
        end_max_heap = queue.PriorityQueue(n)
        for i, line in enumerate(intervals):
            start_max_heap.put((-line[0], {"index": i, "start": line[0]}))
            end_max_heap.put((-line[1], {"index": i, "end": line[1]}))

        # end_array = []
        # start_array = []
        # for _ in range(n):
        #     start_array.append(start_max_heap.get())
        #     end_array.append(end_max_heap.get())
        # print(start_array)
        # print(end_array)

        ans = [-1] * n

        return ans


if __name__ == '__main__':
    obj = Solution()
    # sol1 = obj.findRightInterval_v1([[1, 4], [2, 3], [3, 4]])
    # print(f'expect=[-1,2,-1], actual={sol1}\n')
    #
    sol2 = obj.findRightInterval_v3([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]])
    print(f'expect=[3,3,3,4,5,-1], actual={sol2}\n')

    # sol3 = obj.findRightInterval_v2([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]])
    # print(f'expect=[3,3,3,4,5,-1], actual={sol3}\n')
