class Solution:
    # https://leetcode.com/problems/decode-ways/

    # https://leetcode.com/problems/decode-ways/solutions/608268/python-thinking-process-diagram-dp-dfs/
    # backtrack 或 dfs 記得要思考
    # 是否有剪枝的可能性
    # 不管是用條件判斷剪枝, or 重複子問題 memo 剪枝

    # DFS 算法，关注点在节点
    # 回溯算法，关注点在树枝
    # https://labuladong.github.io/algo/2/22/50/
    def numDecodings_dp(self, s: str) -> int:
        if s[0] == '0':
            return 0

        numbers = set([str(x) for x in range(1, 27)])
        length = len(s)

        # 到第 i 個字符, 有幾個編碼方式
        dp = [0] * length

        # base case
        dp[0] = 1
        if s[0:2] in numbers:
            dp[1] = 2

        for i in range(2, length):
            n1 = s[i]
            if n1 in numbers:
                dp[i] += dp[i - 1]

            n2 = s[i - 1:i + 1]
            if n2 in numbers:
                dp[i] += dp[i - 2]

        print(f'dp = {dp}')
        return dp[-1]

    def numDecodings(self, s: str) -> int:
        self.numbers = set([str(x) for x in range(1, 27)])
        self.ans = 0
        length = len(s)

        meme = [-1] * length
        ans2 = self.dfs(s, 0, [], length, meme)
        print(f'memo = {meme}')
        return ans2

        # self.dfs_timeout(s, 0, [], length)
        # return self.ans

    def dfs(self, s, start, track, length, memo) -> int:
        # 想要進行 memo 剪枝
        # 需要 input output 的對應關係
        # 所以要改寫 dfs_timeout, 讓 memo 發揮作用

        if start == length:
            # print(track)
            return 1

        if memo[start] != -1:
            return memo[start]

        ans = 0
        n1 = s[start]
        if n1 in self.numbers:
            track.append(n1)
            ans += self.dfs(s, start + 1, track, length, memo)
            track.pop()

        if start == length - 1:
            return ans

        n2 = s[start:start + 2]
        if n2 in self.numbers:
            track.append(n2)
            ans += self.dfs(s, start + 2, track, length, memo)
            track.pop()

        memo[start] = ans
        return ans

    def dfs_timeout(self, s, start, track, length):
        if start == length:
            # print(track)
            self.ans += 1
            return

        n1 = s[start]
        if n1 in self.numbers:
            # track.append(n1)
            self.dfs_timeout(s, start + 1, track, length)
            # track.pop()

        if start == length - 1:
            return

        n2 = s[start:start + 2]
        if n2 in self.numbers:
            # track.append(n2)
            self.dfs_timeout(s, start + 2, track, length)
            # track.pop()

    def backtrack_fail(self, s, start, track, length):
        # 此題不是 組合的概驗
        # 組合是 c n 取 k, 會跳過中間的元素
        # 一路往下 且 連續, 應該用 dfs

        if start == length:
            print(track)
            self.ans += 1
            return
        elif start > length:
            return

        for i in range(start, length):
            n1 = s[i]
            if n1 in self.numbers:
                track.append(n1)
                self.backtrack_fail(s, i + 1, track, length)
                track.pop()

        # if start == 0:
        #     return
        #
        # n2 = s[start - 1:start + 1]
        # if n2 in self.numbers:
        #     track.append(n2)
        #     self.backtrack_fail(s, start + 2, track, length)
        #     track.pop()


if __name__ == '__main__':
    # print(Solution().numDecodings("226"))
    # print(Solution().numDecodings("206"))
    # print(Solution().numDecodings("2116"))
    print(Solution().numDecodings("111111111111111111111111111111111111111111111"))

    # print(Solution().numDecodings_dp("2116"))
    print(Solution().numDecodings_dp("111111111111111111111111111111111111111111111"))
