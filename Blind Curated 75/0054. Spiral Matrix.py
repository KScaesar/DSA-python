from typing import List


class Solution:
    # https://leetcode.com/problems/spiral-matrix/description/

    # https://labuladong.github.io/algo/2/20/26/

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        acc = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

        # init value
        # 注意 up 邊界初始為 1
        limit = {"up": 1, "down": m - 1, "left": 0, "right": n - 1}
        cursor = {"col": 0, "row": 0}
        direction = acc["right"]

        # 逆向生成的程式碼, 只要替換這幾行, 其他不用動
        # matrix2 = [[0] * m for _ in range(n)]
        # for v in range(m * n):
        #     matrix2[cursor["row"]][cursor["col"]] = v

        ans = []
        for _ in range(m * n):
            val = matrix[cursor["row"]][cursor["col"]]
            ans.append(val)

            # 邊界 和 方向 都符合條件才轉向
            if cursor["col"] == limit["right"] and direction == acc["right"]:
                direction = acc["down"]
                limit["right"] -= 1
            elif cursor["row"] == limit["down"] and direction == acc["down"]:
                direction = acc["left"]
                limit["down"] -= 1
            elif cursor["col"] == limit["left"] and direction == acc["left"]:
                direction = acc["up"]
                limit["left"] += 1
            elif cursor["row"] == limit["up"] and direction == acc["up"]:
                direction = acc["right"]
                limit["up"] += 1

            cursor["col"] += direction[0]
            cursor["row"] += direction[1]

        return ans

    def spiralOrder_fail(self, matrix: List[List[int]]) -> List[int]:
        # 失敗原因
        # 起點就已經在 邊界條件
        # 卻沒有進行邊界判斷 就直接改變方向

        m = len(matrix)
        n = len(matrix[0])
        total = m * n
        acc = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}

        # init value
        limit = {"up": 1, "down": m - 1, "left": 0, "right": n - 1}
        cursor = {"col": 0, "row": 0}
        direction = acc["right"]

        ans = []
        for _ in range(total):
            val = matrix[cursor["row"]][cursor["col"]]
            ans.append(val)

            # 應該先判斷邊界
            # 再改變方向
            cursor["col"] += direction[0]
            cursor["row"] += direction[1]

            if cursor["col"] == limit["right"] and direction == acc["right"]:
                direction = acc["down"]
                limit["right"] -= 1
            elif cursor["row"] == limit["down"] and direction == acc["down"]:
                direction = acc["left"]
                limit["down"] -= 1
            elif cursor["col"] == limit["left"] and direction == acc["left"]:
                direction = acc["up"]
                limit["left"] += 1
            elif cursor["row"] == limit["up"] and direction == acc["up"]:
                direction = acc["right"]
                limit["up"] += 1

        return ans


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(Solution().spiralOrder([[3], [2]]))
