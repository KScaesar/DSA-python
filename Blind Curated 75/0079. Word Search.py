from typing import List


class Solution:
    # https://leetcode.com/problems/word-search/
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        first = word[0]
        self.acc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                if board[r][c] == first:
                    board[r][c] = ''
                    if self.dfs(board, m, n, (c, r), first, word):
                        return True
                    board[r][c] = first

        return False

    def dfs(self, board, m, n, start, track, target) -> bool:
        if track == target:
            return True
        elif len(track) == len(target) and track != target:
            return False

        for d in self.acc:
            col, row = start
            next_col = col + d[0]
            next_row = row + d[1]
            if next_col < 0 or next_col == n or next_row < 0 or next_row == m:
                continue
            if board[next_row][next_col] == '':
                continue

            char = board[next_row][next_col]
            # print(target[len(track)], len(track) + 1, start, track, char)
            if target[len(track)] != char:
                continue

            board[next_row][next_col] = ''
            if self.dfs(board, m, n, (next_col, next_row), track + char, target):
                return True
            board[next_row][next_col] = char

        return False

    def dfs_timeout(self, board, m, n, start, track, target) -> bool:
        # O(4^k)
        # k = len(target)

        if len(track) == len(target) and track == target:
            return True
        elif len(track) == len(target) and track != target:
            return False

        for d in self.acc:
            col, row = start
            next_col = col + d[0]
            next_row = row + d[1]
            if next_col < 0 or next_col == n or next_row < 0 or next_row == m:
                continue
            if board[next_row][next_col] == '':
                continue

            char = board[next_row][next_col]
            board[next_row][next_col] = ''
            if self.dfs_timeout(board, m, n, (next_col, next_row), track + char, target):
                return True
            board[next_row][next_col] = char

        return False


if __name__ == '__main__':
    print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    # print(Solution().exist([["a", "a"]], "aaa"))
