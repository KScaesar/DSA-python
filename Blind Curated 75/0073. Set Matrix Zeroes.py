from typing import List


class Solution:
    # https://leetcode.com/problems/set-matrix-zeroes/

    # https://leetcode.com/problems/set-matrix-zeroes/solutions/177436/set-matrix-zeroes/

    def setZeroes_v2(self, matrix: List[List[int]]) -> None:
        # https://blog.csdn.net/zml66666/article/details/115058471

        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row_zero = True
                    if j == 0:
                        first_col_zero = True
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 避免影響第一個元素, 都從 1 出發
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if first_col_zero:
            for i in range(0, m):
                matrix[i][0] = 0
        if first_row_zero:
            for j in range(0, n):
                matrix[0][j] = 0

        return

    def setZeroes_v2_fail(self, matrix: List[List[int]]) -> None:
        # 把 上頂點 左頂點 設置為 0 進行標記

        # 太多錯誤了, 重寫函數

        m = len(matrix)
        n = len(matrix[0])

        # 特殊點位
        # 避免被 mark 標記影響
        origin_is_zero = matrix[0][0] == 0

        for k in range(m * n):
            row = k // n
            col = k % n
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

        # 保留 matrix[0][0~n]
        # 避免後續的判斷被影響
        # 因為 col mark 標記, 都放在 第一個 row
        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(n):
                    matrix[row][col] = 0

        for col in range(n):
            if matrix[0][col] == 0:
                for row in range(m):
                    matrix[row][col] = 0

        # 最後再來處理 第一個 row
        #
        # 發現是錯誤的處理方式
        # if matrix[0][0] == 0:
        #     for col in range(n):
        #         matrix[0][col] = 0

        # 需要事先紀錄, 避免標記的時候, 被影響
        if origin_is_zero:
            for col in range(n):
                matrix[0][col] = 0

    def setZeroes_v1(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        # 此定義為 共有幾個點可能是 0
        # 會造成 空間複雜度為 O(M*N)
        #
        # 如果把 zero_points 分成 zero_col_ser, zero_row_set
        # 兩個 set 大小不可能超過 m 和 n
        # Space Complexity: O(M+N)
        zero_points = []

        for k in range(m * n):
            row = k // n
            col = k % n
            if matrix[row][col] == 0:
                zero_points.append((col, row))

        # print(zero_points)

        # 方法1 Space Complexity: O(M*N)
        for point in zero_points:
            col, row = point
            for x in range(n):
                matrix[row][x] = 0
            for y in range(m):
                matrix[y][col] = 0

        # 方法2 Space Complexity: O(M+N)
        #
        # zero_col = [x[0] for x in zero_points]
        # zero_row = [x[1] for x in zero_points]
        # for row in range(m):
        #     for col in range(n):
        #         if col in zero_col or row in zero_row:
        #             matrix[row][col] = 0

        return

    def setZeroes_fail(self, matrix: List[List[int]]) -> None:
        # 誤解題目了
        # 以為只有周圍設置 0, 但題目要求 該位置所在的行列 都要設置為 0
        # 且後來變為 0 的元素, 不會進行 擴散 0 的行為

        m = len(matrix)
        n = len(matrix[0])
        acc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0:
                    continue

                for d in acc:
                    _next = {
                        "x": col + d[0],
                        "y": row + d[1],
                    }
                    if 0 <= _next["x"] <= n - 1 and 0 <= _next["y"] <= m - 1:
                        matrix[_next["y"]][_next["x"]] = 0

        return


if __name__ == '__main__':
    # input1 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    input1 = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    Solution().setZeroes_v1(input1)
    print(input1)

    # input2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    input2 = [[1, 2, 3, 4], [5, 0, 7, 8], [0, 10, 11, 12], [13, 14, 15, 0]]
    Solution().setZeroes_v2(input2)
    print(input2)
