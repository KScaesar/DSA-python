import collections
from typing import List


class Solution:
    # https://www.lintcode.com/problem/892/
    # https://medium.com/@ChYuan/leetcode-269-alien-dictionary-%E5%BF%83%E5%BE%97-hard-7b04656b7569
    # https://www.youtube.com/watch?v=ZU7fiX0WCCY

    # graph, Topological sort

    # https://ithelp.ithome.com.tw/articles/10294471
    # testcase 要满足alien序的同时、余下的解要按照字典序。那就得用minHeap
    # 需要另外紀錄每個節點 in degree 的數值

    # 光是題目就看不懂在表達什麼意思
    # 重點是理解 新語言的字符順序, 是什麼意思 ( However, the order among letters are unknown to you.

    # https://www.youtube.com/watch?v=ZU7fiX0WCCY

    def alien_order(self, words: List[str]) -> str:
        size = len(words)
        if size == 1:
            return ""

        _graph = collections.defaultdict(list)
        inDegree = collections.defaultdict(int)

        # 一般語言寫法
        # for i in range(1, size):
        #     smaller, n1 = "", len(words[i - 1])
        #     greater, n2 = "", len(words[i])
        #     for j in range(n1):
        #         if j >= n2:
        #             return ""
        #
        #         smaller, greater = words[i - 1][j], words[i][j]
        #         if smaller != greater:
        #             _graph[smaller].append(greater)
        #             inDegree[greater] += 1
        #             break

        # py 特殊寫法, 兩個相鄰元素進行對比
        for word1, word2 in zip(words[:-1], words[1:]):
            for smaller, greater in zip(word1, word2):
                if smaller != greater:
                    _graph[smaller].append(greater)
                    inDegree[greater] += 1
                    break

        def dfs(_graph: dict[str, list[str]], cursor: str, path: set, result: list[str]):
            nonlocal has_cycle
            if has_cycle or cursor in path:
                has_cycle = True
                return ""

            path.add(cursor)
            for c in _graph[cursor]:
                dfs(_graph, c, path, result)
            path.remove(cursor)

            result.append(cursor)

        # print(_graph)
        has_cycle = False
        ans = []
        keys = list(_graph.keys())
        for c in keys:
            order = []
            if has_cycle:
                return ""

            dfs(_graph, c, set(), order)

            # print(f' start={c} order={order}')
            if len(ans) < len(order):
                ans = order

        return "".join(ans)[::-1]


if __name__ == '__main__':
    print(Solution().alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
    # print(Solution().alien_order(["z", "x"]))
    # print(Solution().alien_order(["z", "x", "z"]))
