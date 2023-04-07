from typing import List


class Solution:
    # https://leetcode.com/problems/split-array-largest-sum/

    # 將 nums 數組劃分為 k 個子數組，要求每個子數組的和不為空，
    # 且其中一個子數組的元素和是所有子數組中最大的，要最小化這個最大子數組的和。

    # 最大值最小化问题
    # 在最小满足条件的情况下的最大值

    # https://juejin.cn/post/6862249637161091085
    # 需要找到一种拆分，使得这个最大值 val 的值是所有分成 m 段拆分里值最小的那个
    #
    # 使用二分查找的一个前提是「数组具有单调性」
    # 如果某个 数组各自和的最大值 恰恰好使得分割数为 m ，此时不能放弃搜索，因为我们要使得这个最大值 最小化
    # 特别留意题目中出现的关键字「非负整数」、分割「连续」

    # https://books.halfrost.com/leetcode/ChapterFour/0400~0499/0410.Split-Array-Largest-Sum/
    # 可以用动态规划 DP 解答，也可以用二分搜索来解答

    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2

            # 劃分的子數列愈多, 子數列和越小, 所以目標是, 分組數量盡可能的多 mid <= k
            if cnt_le_k(nums, mid, k):
                # 如果真的不知道 ans
                # 要放在 left or right 更新, 就隨便放其中一邊
                # 直接跑測試進行驗證, 不要花太多時間想
                ans = mid
                right = mid - 1
            else:
                # 如果分割数太多，说明「子数组各自的和的最大值」太小
                # 需要将「子数组各自的和的最大值」调大
                left = mid + 1

        return ans


def cnt_le_k(nums, mid_value, k) -> bool:
    cnt, total = 1, 0
    for v in nums:
        total += v
        if total > mid_value:  # 重要分組條件, 使用大於來判斷
            total = v
            cnt += 1

    print(mid_value, cnt, k)

    return cnt <= k


if __name__ == '__main__':
    print(Solution().splitArray([7, 2, 5, 10, 8], 2))
