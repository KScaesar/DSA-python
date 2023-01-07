from typing import List

import tool


class Solution:
    # https://leetcode.com/problems/pacific-atlantic-water-flow/

    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0417.%E5%A4%AA%E5%B9%B3%E6%B4%8B%E5%A4%A7%E8%A5%BF%E6%B4%8B%E6%B0%B4%E6%B5%81%E9%97%AE%E9%A2%98.md

    def pacificAtlantic_v3(self, heights: List[List[int]]) -> List[List[int]]:
        # 空間 O(m*n)
        # 時間 O(m*n)
        #
        # dfs 單個 cell 尋訪的時間是 O(m*n)
        # 本題用了 兩個 for 迴圈, 也許會想成 O(n*m*n + m*m*n)
        # 但實際上有 visited 避免重複尋訪
        # 每個 cell 只會尋訪兩次 分別是 ocean 為 pacific, atlantic 的情況
        # 所以時間是 O(2*m*n)
        #
        # v1 的時間 因為 每個cell都進行一次 dfs
        # 時間是 O(m*n * m*n) 四次方的複雜度

        # v1, v2 使用哪個 cell 可以順利流水到海洋的想法
        # 尋訪每一個點
        #
        # v3 使用 哪些 cell 可以逆流而上
        # 首先 4個邊 肯定是確定可以往上爬, 且四個邊的位置 也決定了 最後流向哪個海域
        # 所以從邊作為起點出發, 之後 dfs 尋訪每個 cell, 肯定也屬於同一個海域
        # 不需要 像是 v1,v2 另外進行判斷流入那個海域
        #
        # v3 寫起來最簡潔
        #
        # v1 利用 start 紀錄的時候, 應該就可以想到
        # 是否有別的想法, 轉換尋訪條件
        # 而不是死死跟隨題目給的往下流水的條件

        def dfs(heights, cursor, ocean):
            if cursor in ocean:
                return

            ocean.add(cursor)

            for d in directions:
                row, col = cursor
                next_row, next_col = row + d[0], col + d[1]
                if is_inbound(next_row, next_col) and heights[row][col] <= heights[next_row][next_col]:
                    dfs(heights, (next_row, next_col), ocean)

        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        is_inbound = lambda row, col: 0 <= row < m and 0 <= col < n

        for r in range(m):
            dfs(heights, (r, 0), pacific)
            dfs(heights, (r, n - 1), atlantic)
        for c in range(n):
            dfs(heights, (0, c), pacific)
            dfs(heights, (m - 1, c), atlantic)

        return list(pacific & atlantic)

    def pacificAtlantic_v2(self, heights: List[List[int]]) -> List[List[int]]:
        def flow_to_which_ocean(heights, cursor, visited, memo) -> list[str] | None:
            if cursor in visited:
                return []

            memo[cursor] = memo.get(cursor, [])

            # 移動到 for 迴圈進行判斷
            # if len(memo[cursor]) == 2:
            #     return memo[cursor]

            row = cursor[0]
            col = cursor[1]
            if not is_inbound(row, col):
                if is_pacific(row, col):
                    return ['p']
                elif is_atlantic(row, col):
                    return ['a']

            visited.add(cursor)

            for d in directions:
                # 改為 從這裡判斷
                if len(memo[cursor]) == 2:
                    break

                next_row = row + d[0]
                next_col = col + d[1]

                if not is_inbound(next_row, next_col) or heights[row][col] >= heights[next_row][next_col]:
                    for ocean in flow_to_which_ocean(heights, (next_row, next_col), visited, memo):
                        if ocean in memo[cursor]:
                            continue

                        if ocean == 'p':
                            pacific.add(cursor)
                        elif ocean == 'a':
                            atlantic.add(cursor)
                        memo[cursor].append(ocean)

            return memo[cursor]

        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        is_inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        is_pacific = lambda row, col: row < 0 or col < 0
        is_atlantic = lambda row, col: row >= m or col >= n

        memo = dict()
        for row in range(m):
            for col in range(n):
                flow_to_which_ocean(heights, (row, col), set(), memo)

        return list(pacific & atlantic)

    def pacificAtlantic_v2_fail_2(self, heights: List[List[int]]) -> List[List[int]]:
        def flow_to_which_ocean(heights, cursor, visited, memo) -> list[str] | None:
            if cursor in visited:
                return []

            memo[cursor] = memo.get(cursor, [])
            if len(memo[cursor]) == 2:
                return memo[cursor]

            row = cursor[0]
            col = cursor[1]
            if not is_inbound(row, col):
                if is_pacific(row, col):
                    return ['p']
                elif is_atlantic(row, col):
                    return ['a']

            visited.add(cursor)

            # 錯誤原因2
            # 應該從 memo 找出 已經有哪些海洋
            # 用一個全新的 ans
            # 找出的海洋, 可能早就存在於 memo
            ans = []
            for d in directions:
                if len(ans) == 2:
                    break

                next_row = row + d[0]
                next_col = col + d[1]

                if not is_inbound(next_row, next_col) or heights[row][col] >= heights[next_row][next_col]:
                    for ocean in flow_to_which_ocean(heights, (next_row, next_col), visited, memo):
                        # 錯誤原因1
                        if ocean in ans:
                            continue

                        if ocean == 'p':
                            pacific.add(cursor)
                        elif ocean == 'a':
                            atlantic.add(cursor)
                        ans.append(ocean)

            for v in ans:
                memo[cursor].append(v)
            return ans

        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        is_inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        is_pacific = lambda row, col: row < 0 or col < 0
        is_atlantic = lambda row, col: row >= m or col >= n

        memo = dict()
        for row in range(m):
            for col in range(n):
                flow_to_which_ocean(heights, (row, col), set(), memo)

        return list(pacific & atlantic)

    def pacificAtlantic_v2_fail_1(self, heights: List[List[int]]) -> List[List[int]]:
        # 失敗原因
        # visited 不應該 充當 memo 的用途
        # 兩者必須明顯區別

        # 且當 memo 有找到解答的時候, 只要答案不滿足兩個海洋
        # 都要嘗試往下一個 cell 尋找新的可能
        # 避免錯失某些路徑

        def flow_to_which_ocean(heights, cursor, visited) -> list[str] | None:
            if cursor in visited:
                # 直接 return, 會錯失某些路徑
                #
                #    3   3   3
                #    3   1   3
                #    0   2   4
                # 比如從 (0,2) 進行 dfs 到達 (1,2)
                # 此時 (0,2) 還沒找到 任何海洋, 正在等 (1,2) 找出結果才會有往下一個 cell
                #
                # 當 (1,2) 也要找下一個 cell 的時候
                # 又回到 (0,2) 此時直接回傳 空陣列[]
                # 於是 (1,2) 只找到了 一個海洋
                # 這個結果之後被 (0,2) 接收後
                # (0,2) 往下一個 cell 找其他海洋
                # 最後 (0.2) 找到兩個海洋
                # 本次的 dfs 徹底結束
                #
                # 當下次的dfs起點 來到 (1,2)
                # 會發現尋訪過了, 於是直接回傳一個海洋的答案
                # 不嘗試往下一個 cell 尋找新的可能
                return visited[cursor]

            row = cursor[0]
            col = cursor[1]
            if not is_inbound(row, col):
                if is_pacific(row, col):
                    return ['p']
                elif is_atlantic(row, col):
                    return ['a']

            # visited 在此函數, 類似 dp 函數中的 memo
            visited[cursor] = visited.get(cursor, [])

            ans = []
            for d in directions:
                if len(ans) == 2:
                    return ['p', 'a']

                next_row = row + d[0]
                next_col = col + d[1]

                if not is_inbound(next_row, next_col) or heights[row][col] >= heights[next_row][next_col]:
                    for ocean in flow_to_which_ocean(heights, (next_row, next_col), visited):
                        # 重點: 不同路徑, 可能進入同一個海域
                        # 如果不跳過, 對 ans 放同樣的答案
                        # 迴圈最上方 判斷長度 = 2 的情境就會失靈
                        if ocean in ans:
                            continue

                        if ocean == 'p':
                            pacific.add(cursor)
                            visited[cursor].append('p')
                        elif ocean == 'a':
                            atlantic.add(cursor)
                            visited[cursor].append('a')
                        ans.append(ocean)

            return ans

        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        is_inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        is_pacific = lambda row, col: row < 0 or col < 0
        is_atlantic = lambda row, col: row >= m or col >= n

        visited = dict()
        for row in range(m):
            for col in range(n):
                flow_to_which_ocean(heights, (row, col), visited)

        return list(pacific & atlantic)

    def pacificAtlantic_v1(self, heights: List[List[int]]) -> List[List[int]]:
        # 尋訪太多次 重複路徑 效率不好
        # 答案是對的
        def dfs(heights, start, cursor, visited):
            if cursor in visited:
                return

            row = cursor[0]
            col = cursor[1]
            if not is_inbound(row, col):
                if is_pacific(*cursor):
                    pacific.add(start)
                elif is_atlantic(*cursor):
                    atlantic.add(start)
                return

            visited.add(cursor)

            for d in directions:
                next_row = row + d[0]
                next_col = col + d[1]
                if not is_inbound(next_row, next_col) or heights[row][col] >= heights[next_row][next_col]:
                    dfs(heights, start, (next_row, next_col), visited)

        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        is_inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        is_pacific = lambda row, col: row < 0 or col < 0
        is_atlantic = lambda row, col: row >= m or col >= n

        for row in range(m):
            for col in range(n):
                dfs(heights, (row, col), (row, col), set())

        # 寫法 1
        # return list(pacific.intersection(atlantic))

        # 寫法 2
        return list(pacific & atlantic)


if __name__ == '__main__':
    # print(Solution().pacificAtlantic_v1([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
    # print(Solution().pacificAtlantic_v2([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))

    # heights_2 = [[3, 3, 3], [3, 1, 3], [0, 2, 4]]
    # tool.print_matrix(heights_2)
    # print(sorted(Solution().pacificAtlantic_v1(heights_2)))
    # print(sorted(Solution().pacificAtlantic_v2(heights_2)))
    # print(sorted(Solution().pacificAtlantic_v3(heights_2)))

    heights_3 = [
        [14, 19, 9, 19, 9, 7, 12, 15, 1, 6, 18, 12, 0, 12, 10, 3, 17, 16, 1, 5, 2, 12, 1, 0, 17, 6, 15, 11, 19, 2, 6, 14, 13, 16, 15, 4, 7,
         6, 16],
        [0, 10, 11, 5, 4, 8, 19, 17, 4, 7, 11, 13, 16, 12, 2, 3, 17, 16, 14, 8, 5, 18, 2, 18, 11, 15, 4, 12, 5, 2, 1, 10, 14, 11, 13, 8, 0,
         3, 8],
        [11, 14, 14, 5, 8, 8, 10, 7, 10, 16, 8, 10, 7, 9, 10, 1, 14, 15, 16, 16, 4, 13, 19, 13, 6, 19, 12, 12, 11, 4, 9, 15, 11, 9, 3, 13,
         19, 13, 8],
        [19, 0, 12, 19, 9, 16, 19, 7, 7, 0, 1, 5, 8, 0, 0, 14, 5, 19, 4, 5, 15, 19, 17, 14, 7, 2, 16, 4, 3, 1, 19, 17, 13, 2, 6, 12, 7, 15,
         3],
        [12, 6, 2, 11, 4, 0, 15, 11, 11, 14, 7, 5, 2, 12, 7, 18, 5, 0, 5, 9, 11, 10, 3, 3, 2, 5, 12, 3, 11, 0, 5, 6, 2, 0, 13, 11, 19, 9,
         2],
        [4, 1, 15, 8, 13, 8, 2, 4, 7, 19, 4, 6, 6, 11, 4, 19, 16, 11, 17, 14, 12, 4, 8, 18, 19, 1, 13, 5, 14, 17, 5, 4, 17, 17, 17, 8, 17,
         2, 17],
        [1, 17, 11, 0, 18, 0, 12, 8, 0, 6, 11, 14, 8, 0, 12, 11, 4, 10, 12, 6, 18, 0, 14, 1, 10, 6, 11, 8, 9, 5, 0, 9, 6, 14, 2, 18, 9, 6,
         6],
        [18, 3, 5, 11, 18, 6, 18, 13, 1, 6, 11, 12, 10, 16, 0, 18, 10, 3, 9, 14, 7, 12, 5, 14, 6, 16, 4, 0, 2, 7, 2, 9, 2, 19, 14, 14, 9,
         12, 5],
        [17, 6, 17, 15, 13, 6, 15, 3, 5, 18, 19, 8, 11, 18, 2, 1, 8, 12, 3, 3, 8, 19, 15, 18, 9, 4, 1, 4, 18, 6, 13, 18, 3, 6, 19, 13, 10,
         18, 2],
        [5, 12, 7, 11, 19, 5, 10, 17, 0, 7, 7, 9, 1, 11, 18, 11, 7, 3, 4, 19, 12, 17, 2, 3, 1, 19, 5, 8, 13, 8, 1, 11, 6, 9, 3, 14, 16, 14,
         3],
        [14, 11, 9, 7, 4, 4, 5, 2, 9, 1, 2, 2, 4, 12, 7, 0, 8, 17, 9, 15, 14, 4, 18, 19, 17, 2, 18, 8, 8, 5, 7, 0, 4, 10, 12, 5, 8, 8, 2],
        [12, 7, 7, 18, 2, 6, 2, 13, 9, 5, 15, 1, 0, 4, 5, 5, 5, 11, 16, 18, 8, 18, 17, 11, 1, 9, 13, 7, 19, 12, 7, 17, 15, 15, 2, 19, 16,
         13, 9],
        [19, 4, 19, 4, 3, 0, 3, 4, 1, 3, 2, 10, 5, 9, 4, 8, 16, 7, 0, 12, 2, 6, 8, 11, 10, 12, 19, 10, 9, 12, 1, 18, 13, 18, 8, 17, 12, 8,
         13],
        [17, 14, 8, 11, 2, 4, 1, 8, 11, 15, 2, 1, 2, 5, 6, 5, 15, 15, 3, 1, 3, 8, 10, 19, 0, 18, 15, 17, 5, 7, 2, 14, 13, 7, 5, 12, 16, 9,
         6],
        [13, 5, 15, 17, 15, 0, 0, 15, 18, 19, 2, 19, 14, 5, 13, 10, 19, 7, 19, 14, 14, 15, 4, 7, 1, 19, 1, 17, 14, 18, 18, 3, 0, 18, 6, 9,
         15, 10, 16],
        [10, 0, 0, 15, 8, 10, 15, 14, 16, 3, 11, 11, 7, 3, 18, 19, 3, 10, 11, 3, 1, 5, 10, 5, 11, 15, 2, 5, 5, 6, 7, 15, 17, 18, 17, 0, 15,
         13, 3],
        [9, 8, 6, 17, 3, 7, 3, 3, 8, 3, 13, 10, 11, 16, 17, 5, 12, 16, 17, 6, 3, 18, 14, 13, 19, 13, 0, 18, 11, 19, 7, 3, 9, 3, 9, 19, 19,
         6, 0],
        [10, 15, 17, 7, 18, 2, 3, 5, 19, 6, 9, 11, 9, 18, 3, 8, 10, 15, 11, 7, 11, 8, 18, 19, 19, 18, 11, 6, 8, 6, 3, 9, 6, 5, 19, 8, 14,
         15, 9],
        [19, 8, 7, 14, 4, 19, 3, 17, 8, 11, 19, 17, 18, 9, 1, 13, 3, 17, 4, 1, 17, 1, 17, 10, 13, 1, 13, 3, 3, 3, 12, 15, 18, 11, 12, 2, 5,
         1, 17],
        [11, 2, 16, 4, 17, 17, 7, 8, 6, 6, 15, 4, 6, 16, 4, 8, 16, 5, 1, 3, 3, 12, 7, 18, 4, 5, 10, 15, 3, 9, 18, 5, 18, 14, 16, 16, 1, 13,
         13],
        [9, 17, 7, 2, 5, 0, 14, 12, 7, 9, 10, 11, 3, 5, 12, 17, 8, 5, 14, 19, 18, 16, 8, 2, 7, 17, 4, 13, 13, 7, 6, 8, 5, 5, 11, 2, 6, 4,
         16],
        [9, 1, 16, 10, 3, 5, 3, 18, 9, 3, 9, 3, 2, 4, 17, 15, 5, 6, 9, 19, 9, 9, 5, 19, 7, 8, 7, 15, 11, 9, 3, 0, 16, 18, 6, 18, 0, 5, 19],
        [6, 3, 15, 5, 5, 17, 17, 2, 10, 4, 11, 2, 13, 17, 18, 9, 8, 2, 10, 10, 1, 1, 17, 19, 14, 11, 8, 18, 14, 15, 4, 19, 13, 16, 19, 5, 0,
         14, 17],
        [3, 7, 18, 14, 15, 12, 12, 7, 13, 1, 2, 18, 15, 18, 11, 18, 14, 8, 5, 5, 5, 10, 16, 4, 9, 3, 11, 13, 0, 4, 10, 0, 16, 4, 19, 18, 4,
         6, 12],
        [5, 11, 19, 17, 13, 13, 2, 18, 17, 10, 17, 3, 17, 6, 14, 19, 3, 7, 2, 8, 14, 7, 9, 1, 11, 5, 13, 12, 16, 7, 1, 3, 18, 2, 2, 1, 7, 5,
         9],
        [10, 16, 1, 14, 19, 2, 2, 2, 8, 8, 16, 12, 0, 5, 13, 3, 11, 8, 2, 12, 8, 8, 9, 14, 10, 11, 13, 13, 14, 3, 18, 2, 10, 5, 17, 9, 16,
         18, 4],
        [9, 18, 15, 15, 9, 18, 12, 14, 10, 8, 17, 3, 0, 7, 17, 16, 1, 5, 1, 6, 0, 18, 14, 5, 3, 4, 7, 16, 6, 18, 1, 1, 17, 14, 12, 14, 4, 6,
         7],
        [7, 13, 15, 5, 8, 6, 17, 8, 0, 6, 16, 7, 4, 4, 19, 11, 2, 15, 10, 6, 5, 12, 1, 5, 9, 16, 16, 12, 12, 17, 9, 4, 0, 14, 17, 12, 9, 12,
         15],
        [9, 8, 13, 18, 9, 3, 16, 12, 7, 7, 9, 5, 6, 15, 19, 14, 12, 3, 12, 0, 1, 1, 17, 9, 17, 4, 3, 18, 2, 15, 6, 12, 15, 9, 6, 8, 11, 10,
         8],
        [13, 10, 3, 3, 16, 19, 16, 8, 4, 6, 19, 15, 14, 17, 13, 15, 12, 18, 16, 10, 5, 0, 0, 15, 0, 11, 14, 1, 18, 5, 15, 17, 7, 12, 8, 7,
         1, 2, 11],
        [6, 4, 9, 18, 2, 9, 7, 3, 16, 10, 17, 15, 9, 16, 4, 17, 11, 4, 9, 16, 1, 12, 16, 17, 18, 13, 16, 15, 14, 18, 2, 7, 5, 8, 11, 0, 17,
         10, 15],
        [17, 11, 13, 4, 10, 13, 13, 4, 6, 15, 6, 16, 2, 16, 1, 11, 16, 8, 3, 11, 7, 16, 12, 6, 14, 6, 10, 4, 4, 12, 1, 1, 6, 8, 19, 15, 16,
         14, 13],
        [7, 16, 10, 4, 1, 1, 0, 10, 13, 16, 18, 6, 16, 12, 9, 11, 12, 7, 9, 9, 1, 2, 11, 6, 2, 18, 4, 19, 12, 6, 16, 19, 9, 9, 12, 10, 12,
         4, 19],
        [3, 0, 13, 8, 17, 0, 11, 17, 19, 7, 18, 8, 2, 2, 12, 18, 0, 8, 1, 10, 10, 1, 16, 11, 5, 14, 18, 2, 2, 8, 8, 3, 12, 19, 7, 7, 12, 15,
         8],
        [8, 7, 12, 11, 5, 12, 15, 11, 12, 0, 1, 19, 11, 3, 18, 5, 7, 9, 6, 8, 4, 10, 6, 13, 5, 9, 19, 6, 7, 3, 16, 6, 6, 12, 1, 18, 16, 15,
         15],
        [6, 15, 10, 12, 8, 2, 10, 12, 5, 8, 16, 10, 17, 4, 18, 17, 14, 1, 1, 14, 14, 2, 7, 17, 10, 7, 18, 0, 19, 12, 7, 15, 18, 14, 10, 9,
         16, 3, 15],
        [15, 9, 9, 10, 5, 3, 1, 12, 2, 7, 7, 5, 6, 15, 18, 11, 3, 15, 14, 9, 15, 6, 13, 9, 18, 18, 12, 4, 8, 8, 3, 14, 15, 9, 0, 11, 6, 4,
         0],
        [6, 9, 5, 11, 17, 17, 17, 19, 11, 9, 2, 5, 0, 4, 3, 12, 8, 6, 11, 6, 3, 13, 14, 1, 0, 15, 4, 7, 18, 11, 14, 15, 11, 6, 0, 13, 5, 5,
         17]]
    tool.print_matrix(heights_3,
                      targets=[(0, 38), (2, 36), (33, 2), (34, 2), (35, 1), (35, 2), (35, 3), (36, 0), (36, 1), (36, 2), (36, 3), (37, 0),
                               (37, 1), (37, 3), (37, 4), (37, 5), (37, 6), (37, 7)])
    print(sorted(Solution().pacificAtlantic_v1(heights_3)))
    print(sorted(Solution().pacificAtlantic_v2(heights_3)))
    print(sorted(Solution().pacificAtlantic_v3(heights_3)))
