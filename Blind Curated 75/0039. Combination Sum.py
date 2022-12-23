from typing import List


class Solution:
    # https://leetcode.com/problems/combination-sum/

    # https://leetcode.com/problems/combination-sum/solutions/429538/general-backtracking-questions-solutions-in-python-for-reference/?orderBy=most_votes

    # 時間複雜度分析
    # dp 解法 ( 可看成另類的背包問題)
    # https://leetcode.com/problems/combination-sum/solutions/937255/python-3-dfs-backtracking-two-dp-methods-explanations/?orderBy=most_votes
    def combinationSum_dp(self, candidates: List[int], target: int) -> List[List[int]]:
        # 之後練習
        pass

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrackV2(nums, start, track, total):
            nonlocal target, ans

            if total == target:
                ans.append(track.copy())
                return
            elif total > target:
                return

            for i in range(start, len(nums)):
                v = nums[i]
                backtrackV2(nums, i, track + [v], total + v)

        def backtrackV1(nums, start, track):
            nonlocal target, ans

            _sum = sum(track)
            if _sum == target:
                ans.append(track.copy())
                return
            elif _sum > target:
                return

            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrackV1(nums, i, track)
                track.pop()

        backtrackV2(candidates, 0, [], 0)
        return ans


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
    print(Solution().combinationSum_dp([2, 3, 6, 7], 7))
