from typing import List


class Solution:
    # https://leetcode.com/problems/longest-consecutive-sequence/
    def longestConsecutive_v2(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak/

        sets = set(nums)
        ans = 0
        for v in sets:
            # 確定 v 是 起點
            # 才開始運算
            if not v - 1 in sets:
                _next = v + 1
                while _next in sets:
                    _next += 1
                ans = max(ans, _next - v)

        return ans

    def longestConsecutive_dsf(self, nums: List[int]) -> int:
        # https://github.com/halfrost/LeetCode-Go/tree/master/leetcode/0128.Longest-Consecutive-Sequence#%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF

        if len(nums) == 0:
            return 0

        parent = {x: x for x in nums}

        # print(parent)

        def find(node) -> int:
            # print(node)
            if parent[node] != node:
                parent[node] = find(parent[node])

            # return node 要回傳根節點, 而不是回傳子節點
            #
            return parent[node]

        def set_union(node1, node2):
            # print(parent)
            root1 = find(node1)
            root2 = find(node2)

            # 正確作法
            if root1 != root2:
                parent[root2] = root1

            # 錯誤作法
            # 造成需要 往特定方向 union
            # 應該修改 根節點的指向
            # 而不是修改 子節點的指向
            # if root1 != root2:
            #     # 要固定往某個方向
            #     # 不然會 union 失敗
            #     #
            #     # parent[node2] = root1
            #     if node1 > node2:
            #         parent[node2] = root1
            #     else:
            #         parent[node1] = root2

        for v in nums:
            if v - 1 in parent.keys():
                set_union(v, v - 1)
            if v + 1 in parent.keys():
                set_union(v, v + 1)

        # 如果 nums 有相同數字, 只能計算一次
        # 以下方式會重複計算
        # counts = collections.defaultdict(int)
        # for v in nums:
        #     root = find(v)
        #     counts[root] += 1

        counts = {k: 1 for k in parent.keys()}
        # for i in nums: # 錯誤寫法, 用 counts 才能除去重複
        for k in counts:
            root = find(k)
            if root != k:
                counts[root] += 1

        # print(parent)
        # print(counts)
        return max(counts.values())


if __name__ == '__main__':
    print(Solution().longestConsecutive_dsf([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive_dsf([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(Solution().longestConsecutive_dsf([0, 0, -1]))
    print(Solution().longestConsecutive_dsf([0, 0, 1, -1]))
    print()
    print(Solution().longestConsecutive_v2([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive_v2([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(Solution().longestConsecutive_v2([0, 0, -1]))
    print(Solution().longestConsecutive_v2([0, 0, 1, -1]))
