import heapq
from typing import List


# O(ElogV)
#
# E 是因為算法需要遍歷所有邊，以找到最短路徑；
# 而 logV 是因為優先隊列使用了最小堆（min-heap）實現，每次取出最小花費節點需要維護 heap 的平衡


class Solution:
    # 1631. Path With Minimum Effort
    # https://leetcode.com/problems/path-with-minimum-effort/

    # https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/dijkstra-s-6d0b2/

    # 限制中轉次數的寫法
    # https://dengking.github.io/discrete/Data-structure/Graph/Shortest-longest-path/Dijkstra%27s-algorithm/LeetCode-787-K%E7%AB%99%E4%B8%AD%E8%BD%AC%E5%86%85%E6%9C%80%E4%BE%BF%E5%AE%9C%E7%9A%84%E8%88%AA%E7%8F%AD/

    # 不能有效處理帶有負權邊的圖
    # E = edge, V = vertex
    # 使用 heap, time complexity O( (|E|+|V|)*log|V| )
    # https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95

    # 特定頂點到其餘頂點的最短路徑, edge 必須為正, 使用 Dijkstra 算法
    # 特定頂點到其餘頂點的最短路徑, edge 有負號, 使用 Bellman-Ford 算法
    # 如果求任意兩點的路徑, 使用 Floyd 算法
    # https://www.youtube.com/watch?v=JLARzu7coEs

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # https://youtu.be/9wV1VxlfBlI?t=1369

        # O(E*logV)，其中 E 代表图中边的条数，V 代表图中节点的个数。
        # 理想情况下优先级队列中最多装 V 个节点，对优先级队列的操作次数和 E 成正比，所以整体的时间复杂度就是 O(ElogV)

        # 不熟悉的地方:
        # 不清楚 distances, d_path 的更新時機

        m = len(heights)
        n = len(heights[0])
        size = m * n
        DIR = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # 第一次經過某個節點時的路徑權重
        # 不見得就是最小的，所以對於同一個節點，我們可能會經過多次
        #
        # https://www.youtube.com/watch?v=9wV1VxlfBlI&t=1725s
        # bfs 是 push queue 的時候, 把節點標記為 已尋訪
        # 但 dijkstra 是 pop heap, 把節點標示為 已尋訪
        #
        # visited 可能是多餘的, 應該 pop 的時候, 判斷當前 node 的 cost 是否大於 dp 表
        visited = [False] * size

        distances = [float('inf')] * size  # 各個節點和起點的距離, 類似 dp table 的概念
        d_path = [-1] * size  # 單純算距離, 不需要 d_path, 需要特別顯示 路徑過程, 才需要 d_path

        distances[0] = 0
        d_path[0] = 0
        pq_dist = [(0, 0)]  # (distance,node) 由於路徑有權重, 需要每個節點自己紀錄距離, 不像 一般 bfs 可以使用 step 來紀錄
        while pq_dist:
            state = heapq.heappop(pq_dist)
            dist, node = state[0], state[1]
            visited[node] = True

            row, col = node // n, node % n
            for d in DIR:
                next_row, next_col = row + d[0], col + d[1]
                next_node = next_row * n + next_col
                if 0 <= next_row < m and 0 <= next_col < n and not visited[next_node]:
                    diff = abs(heights[next_row][next_col] - heights[row][col])
                    next_dist = dist + diff

                    if distances[next_node] > next_dist:
                        distances[next_node] = next_dist
                        d_path[next_node] = node
                        heapq.heappush(pq_dist, (next_dist, next_node))

        # 此題中評判一條路徑是長還是短的標準
        # 不是路徑經過的權重總和，而是路徑經過的權重最大值
        efforts = [float('inf')] * size
        e_path = [-1] * size

        efforts[0] = 0
        e_path[0] = 0
        pq_effort = [(0, 0)]  # (effort,node)
        while pq_effort:
            state = heapq.heappop(pq_effort)
            effort, node = state[0], state[1]

            # 因为优先级队列自动排序的性质，如果发现这个节点就是终点 end, 肯定是最佳解
            if node == size - 1:
                return efforts[-1]

            # 由於 heap 特性, 後放的節點, 也可能先彈出來, 比較差的路徑, 可以直接跳過
            # 用 heap 就是使用了 貪心的概念
            #
            # 此條件判斷, 類似 visited 的功能
            if effort > efforts[node]:
                continue

            row, col = node // n, node % n
            for d in DIR:
                next_row, next_col = row + d[0], col + d[1]
                if 0 <= next_row < m and 0 <= next_col < n:
                    # 錯誤作法, 沒有和之前的比較, 不能說是到達此節點 曾經的最大努力值
                    # next_effort = abs(heights[next_row][next_col] - heights[row][col])

                    next_effort = max(abs(heights[next_row][next_col] - heights[row][col]), efforts[node])
                    next_node = next_row * n + next_col

                    if efforts[next_node] > next_effort:
                        efforts[next_node] = next_effort
                        e_path[next_node] = node
                        heapq.heappush(pq_effort, (next_effort, next_node))

        print("distances", distances)
        print("d_path", d_path)
        print()
        print("efforts", efforts)
        print("e_path", e_path)
        return efforts[-1]


if __name__ == '__main__':
    print(Solution().minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
    # print(Solution().minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]]))
