from typing import List


class Solution:
    # https://leetcode.com/problems/rotate-image/

    # 算法筆記 p117
    # 如何走訪矩陣 上三角 下三角

    # 如何走訪斜線 Zigzag (or diagonal) traversal
    # https://www.bilibili.com/video/BV1wK4y1j7JU/
    # https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/

    # 旋轉陣列的應用
    # 類數獨遊戲 快速求所有解
    # https://www.facebook.com/groups/1403852566495675/posts/3349253398622239/?comment_id=3349623705251875

    def rotate(self, matrix: List[List[int]]) -> None:
        # 利用矩陣以對角線為中心, 互換的特性
        # https://labuladong.github.io/algo/2/20/26/

        # 時間複雜度分析
        # 以及另一種解法
        # 每次遞迴交換 四個 cell
        # https://leetcode.com/problems/rotate-image/solutions/1037232/rotate-image/?orderBy=most_votes

        size = len(matrix)

        for row in range(size):
            for col in range(row + 1, size):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(size):
            left = 0
            right = size - 1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1


if __name__ == '__main__':
    data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().rotate(data1))
    print(data1)
