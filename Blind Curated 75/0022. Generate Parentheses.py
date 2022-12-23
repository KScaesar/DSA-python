from tool import debug_helper


class Solution:
    def generateParenthesis_v2(self, n: int) -> list[str]:
        # if 左括弧數量 還不等於 n : 可以繼續加 左括弧
        # if 右括弧數量 小於 左括弧數量 : 繼續加 右括弧

        ans = []
        self.dfs(n, 0, 0, '', ans)
        return ans

    @debug_helper
    def dfs(self, n, left, right, track, result):
        if left == right == n:
            result.append(track)
            return

        if left < n:
            self.dfs(n, left + 1, right, track + '(', result)
        if left > right:
            self.dfs(n, left, right + 1, track + ')', result)

    def generateParenthesis(self, n: int) -> list[str]:
        left = ['(' for _ in range(n)]
        right = [')' for _ in range(n)]
        self.symbols = left + right
        self.ans = set()

        self.backtrace(n * 2, [False] * 2 * n, [])
        return list(self.ans)

    def backtrace(self, length: int, used: list[bool], track: list[str]):

        if not self.check_parentheses(track):
            return

        if len(track) == length:
            subset = ''.join(track.copy())
            if subset not in self.ans:
                print(subset)
                self.ans.add(subset)
            return

        for i in range(length):
            if used[i]:
                continue

            # 關鍵剪枝邏輯
            # https://github.com/labuladong/fucking-algorithm/blob/master/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%AD%90%E9%9B%86%E6%8E%92%E5%88%97%E7%BB%84%E5%90%88.md#%E6%8E%92%E5%88%97%E5%85%83%E7%B4%A0%E5%8F%AF%E9%87%8D%E4%B8%8D%E5%8F%AF%E5%A4%8D%E9%80%89
            if i > 0 and not used[i - 1] and self.symbols[i - 1] == self.symbols[i]:
                continue

            used[i] = True
            track.append(self.symbols[i])
            self.backtrace(length, used, track)
            used[i] = False
            track.pop()

    def backtrace_fail2(self, length: int, used: list[bool], track: list[str]):
        # timeout
        if not self.check_parentheses(track):
            return

        if len(track) == length:
            subset = ''.join(track.copy())
            if subset not in self.ans:
                print(subset)
                self.ans.add(subset)
            return

        for i in range(length):
            if used[i]:
                continue

            used[i] = True
            track.append(self.symbols[i])
            self.backtrace_fail2(length, used, track)
            used[i] = False
            track.pop()

    def backtrace_fail(self, length: int, used: list[bool], track: list[str]):
        # output:
        # "((()))","((()))","((()))","((()))","((()))",
        # "((()))","(()())","(()())","(())()","(())()",
        # "(()())","(()())","(())()","(())()","(()())",
        # "(()())", ....

        if not self.check_parentheses(track):
            return

        if len(track) == length:
            # self.ans.append(str.join(track.copy()))
            self.ans.add(''.join(track.copy()))
            return

        for i in range(length):
            if used[i]:
                continue

            used[i] = True
            track.append(self.symbols[i])
            self.backtrace_fail(length, used, track)
            used[i] = False
            track.pop()

    def check_parentheses(self, data: list[str]) -> bool:
        count = 0
        for v in data:
            if v == '(':
                count += 1
            elif v == ')' and count != 0:
                count -= 1
            elif v == ')' and count == 0:
                return False
        return count >= 0


if __name__ == '__main__':
    sol1 = Solution().generateParenthesis_v2(3)
    print(sol1)
