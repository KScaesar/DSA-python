import collections
import string
from typing import List


class Solution:
    # https://leetcode.com/problems/word-break/

    # 重點題目 仔細複習
    def wordBreak_dp(self, s: str, wordDict: List[str]) -> bool:
        # 本題用 解法2 的實做方式
        # 解法1 可以另外看影片解釋

        # dp 解法1 https://youtu.be/5_T7ihU-zdo?t=1084

        # dp 解法2
        # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.md
        # 单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满
        # 拆分时可以重复使用字典中的单词，说明就是一个完全背包
        # 且要求背包的內容有順序性, 也就是需要排列

        # 拆分为一个或多个在字典中出现的单词，所以这是完全背包。
        # 还要讨论两层for循环的前后顺序。
        # 如果求组合数就是外层for循环遍历物品，内层for遍历背包。基本背包問題
        # 如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        #
        # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0518.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2II.md
        #
        # 背包里求排列问题，即：1、2 步 和 2、1 步都是上三个台阶，但是这两种方法不一样！
        # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85%E7%89%88%E6%9C%AC.md

        # 以長度為狀態
        # dp[i] : 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词。
        dp = [False] * (len(s) + 1)
        dp[0] = True  # 假定長度為 0, 一定可以拆分

        # 右開區間, right 也可以看成 長度 len = right - 0(left)
        for right in range(1, len(s) + 1):  # 遍历背包
            for word in wordDict:  # 遍历物品
                size = len(word)
                # if right >= size:
                #     print(f' right={right} now={s[right - size:right]} word={word}')
                #     print([(i, v) for i, v in enumerate(dp)])
                if right >= size and s[right - size:right] == word and dp[right - size]:
                    dp[right] = True

        return dp[-1]

    def wordBreak_bfs(self, s: str, wordDict: List[str]) -> bool:
        # https://youtu.be/5_T7ihU-zdo?t=681
        # timeout 版本

        words = set(wordDict)
        # 第一個元素 0, 表示 s 的 第 0 個索引
        q = collections.deque([0])

        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                idx = q.popleft()
                if idx == len(s):
                    return True

                # 寫法1
                # for word in wordDict:
                #     size = len(word)
                #     if len(s) - idx >= size and s[idx:idx + size] == word:
                #         q.append(idx + size)

                # 寫法2
                for end in range(idx, len(s) + 1):
                    if s[idx:end] in words:
                        q.append(end)

        return False

    def wordBreak_dfs(self, s: str, wordDict: List[str]) -> bool:
        # 雖然影片說 這是 dfs
        # 但我覺得這應該是 dp + memo: top-down 的解法
        #
        # https://youtu.be/5_T7ihU-zdo?t=72
        # 定義 dfs(index) 為 s[index:] 是否可以用 workDict 進行切割
        # dfs(i) = dfs(i + len(w1) or dfs(i + len(w2) or ...
        # dfs(len(s)) = True
        #
        # 後來發現, 這種加了 memo 的方式
        # 歸屬於 dfs, backtrack
        # 动态规划和回溯算法的關係
        # 算法筆記 p213
        # https://labuladong.github.io/algo/di-er-zhan-a01c6/bei-bao-le-34bd4/dong-tai-g-35341/

        memo = dict()

        # @debug_helper
        def dfs(start) -> bool:
            # https://youtu.be/5_T7ihU-zdo?t=226
            # 為什麼設定這個條件, 而不是 len-1, 請看影片
            # 因為當初定義 dfs 為 s[index:],
            # 所以當 index == len(s), 表示已經執行過所有路徑
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for word in wordDict:
                size = len(word)
                if len(s) - start >= size and s[start:start + size] == word:
                    ok = dfs(start + size)
                    if ok:
                        return True

            memo[start] = False
            return False

        return dfs(0)

    def wordBreak_backtrack(self, s: str, wordDict: List[str]) -> bool:
        # 雖然會 timeout
        # 概念類似 backtrack 排列（元素可複選）
        # https://github.com/labuladong/fucking-algorithm/blob/master/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%AD%90%E9%9B%86%E6%8E%92%E5%88%97%E7%BB%84%E5%90%88.md#%E6%8E%92%E5%88%97%E5%85%83%E7%B4%A0%E6%97%A0%E9%87%8D%E5%8F%AF%E5%A4%8D%E9%80%89

        # 應該和 dfs 的方法比較
        # 想想 dfs 的思路是什麼
        # 我只能想到 backtrack 的作法

        ok = False

        # @debug_helper
        def backtrack(track):
            nonlocal ok
            if track == s:
                ok = True
                return
            if len(track) > len(s):
                return

            for word in wordDict:
                if not ok:
                    backtrack(track + word)

        backtrack("")
        return ok

    def wordBreak_v1_fail(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        count = len(s)
        left = 0
        right = 0
        while right < len(s):
            right += 1
            word = s[left:right]
            print(word, count)
            # 每次只會選擇 最低符合標準, 不會依據情況變換
            # 比如 s= aaaaaaa, 可以分成 aaa aaaa
            # 但是此方案 只會選擇 aaa aaa a
            # 目標 words = ["aaaa", "aaa"]
            if word in words:
                _len = right - left
                left = left + _len
                count -= _len
        return count == 0

    def wordBreak_fail2(self, s: str, wordDict: List[str]) -> bool:
        # 又再次誤解題目
        # 題目是問 是否可以 將 s 完全分解為 words 中的 一個 或 多個
        # 沒有說要全部符合

        wordDict.sort(key=lambda x: -len(x))
        used = [False] * len(s)
        for word in wordDict:
            word_size = len(word)
            is_match = False

            for i in range(word_size - 1, len(s)):
                left = i - word_size + 1
                right = i + 1
                if s[left:right] == word:
                    ok = True
                    for k in range(left, right):
                        if used[k]:
                            ok = False
                            break

                    if not ok:
                        break

                    for k in range(left, right):
                        used[k] = True
                    is_match = True
                    break

            # print(used)
            if not is_match:
                return False
        return True

    def wordBreak_fail1(self, s: str, wordDict: List[str]) -> bool:
        # 失敗原因
        # 題目不是單純問 s 是否包含 word

        for word in wordDict:
            word_size = len(word)
            is_match = True
            for i in range(word_size - 1, len(s)):
                left = i - word_size + 1
                right = i + 1
                if s[left:right] == word:
                    is_match = True
            if not is_match:
                return False
        return True

    def wordBreak_kmp(self, s: str, wordDict: List[str]) -> bool:
        # 本題目不適用 kmp
        # 因為題目要求 是否可以將 s 切割為 目標 words
        # 而不是單純問 s 是否包含 word

        for word in wordDict:
            pattern = KMP(word)
            if not pattern.is_match_v2(s):
                return False
        return True


class KMP:
    # https://labuladong.github.io/algo/3/28/97/
    def __init__(self, pattern: str, dictionary: str = string.ascii_letters):
        # self.__create_v1(pattern, dictionary)
        self.__create_v2(pattern)

    def __create_v2(self, pattern: str):
        m = len(pattern)
        if m == 0:
            return

        keys = set(pattern)
        keys.add("other")
        dp = [{c: 0 for c in keys} for _ in range(m)]
        dp[0][pattern[0]] = 1

        prev = 0
        for j in range(1, m):
            for c in keys:
                if pattern[j] == c:
                    dp[j][c] = j + 1
                else:
                    dp[j][c] = dp[prev][c]
            prev = dp[prev][pattern[j]]

        self.dp = dp
        self.pattern = pattern
        for k in range(m):
            print(k, pattern[k], dp[k])

    def is_match_v2(self, text) -> bool:
        m = len(self.pattern)
        pattern_key = self.dp[0].keys()

        j = 0  # pattern index
        for c in text:
            if c in pattern_key:
                j = self.dp[j][c]
            else:
                j = self.dp[j]['other']
            if j == m:
                return True

        return False

    def __create_v1(self, pattern: str, dictionary: str = string.ascii_letters):
        m = len(pattern)
        if m == 0:
            return

        # dp[状态][字符] = 下个状态
        # 初始狀態都指向 第 0 個字符
        dp = [{c: 0 for c in dictionary} for _ in range(m)]

        # base case
        dp[0][pattern[0]] = 1

        # 遇到不匹配字符时, 之前匹配的 index
        # 输入状态机后所能走到的 index
        prev = 0

        for j in range(1, m):
            for c in dictionary:
                if pattern[j] == c:  # 滿足該狀態的條件, 才能前進到下一個狀態
                    dp[j][c] = j + 1
                else:
                    dp[j][c] = dp[prev].get(c)
            prev = dp[prev].get(pattern[j])
            if prev is None:
                raise Exception(f'char = {pattern[j]} not exist in dictionary')

        self.dp = dp
        self.pattern = pattern
        for k in range(m):
            print(k, pattern[k], dp[k])

    def is_match_v1(self, text) -> bool:
        m = len(self.pattern)
        j = 0  # pattern index
        for c in text:
            j = self.dp[j].get(c)
            if j is None:
                msg = f'char = {c} not exist in dictionary'
                raise Exception(msg)

            if j == m:
                return True
        return False


if __name__ == '__main__':
    # print(Solution().wordBreak_backtrack("leetcode", ["leet", "code"]))
    # print(Solution().wordBreak_backtrack("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # print(Solution().wordBreak_backtrack("bb", ["a", "b", "bbb", "bbbb"]))
    # print(Solution().wordBreak_backtrack("aaaaaaa", ["aaaa", "aaa"]))
    # print(Solution().wordBreak_backtrack("cars", ["car", "ca", "rs"]))
    print()

    # print(Solution().wordBreak_dfs("leetcode", ["leet", "code"]))
    print(Solution().wordBreak_dfs("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak_dfs("bb", ["a", "b", "bbb", "bbbb"]))
    print(Solution().wordBreak_dfs("aaaaaaa", ["aaaa", "aaa"]))
    print(Solution().wordBreak_dfs("cars", ["car", "ca", "rs"]))
    print()

    # print(Solution().wordBreak_bfs("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    # print(Solution().wordBreak_bfs("bb", ["a", "b", "bbb", "bbbb"]))
    # print(Solution().wordBreak_bfs("aaaaaaa", ["aaaa", "aaa"]))
    # print(Solution().wordBreak_bfs("cars", ["car", "ca", "rs"]))
    # print()

    print(Solution().wordBreak_dp("catsandog", ["cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak_dp("bb", ["a", "b", "bbb", "bbbb"]))
    print(Solution().wordBreak_dp("aaaaaaa", ["aaaa", "aaa"]))
    print(Solution().wordBreak_dp("cars", ["car", "ca", "rs"]))
    print()

    # pattern = KMP("co1co2coco", dictionary="code123")
    # print(pattern.is_match_v2("123_co1co2coc0"))
