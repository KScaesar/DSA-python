from typing import List


# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/
# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/solutions/4109955/java-c-python-one-pass-count-zero-score/
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        return self.v2(nums)

    def v2(self, nums):
        if self.score(nums) != 0:
            return 1
        ans = 0
        v = -1  # -1 的 二進位表示為 0b11111111, 跟任何數字 and 運算都可以得到原本的數值
        size = len(nums)
        for i in range(size):
            v &= nums[i]
            if v == 0:  # 本身等於 0, 就可以自成一個 subarray
                ans += 1
                v = -1
        return max(1, ans)  # 特殊條件

    def v1(self, nums):
        if self.score(nums) != 0:
            return 1
        ans = 0
        size = len(nums)
        for i in range(size):
            if nums[i] == 0:  # 本身等於 0, 就可以自成一個 subarray
                ans += 1
                continue

            if i < size - 1:
                nums[i + 1] &= nums[i]  # 特殊技巧: 把前一個數值, 累加到下一個
        return max(1, ans)  # 特殊條件

    def score(self, nums) -> int:
        ans = -1  # -1 的 二進位表示為 0b11111111, 跟任何數字 and 運算都可以得到原本的數值
        for i in range(len(nums)):
            ans = ans & nums[i]
        return ans

    def maxSubarrays_fail(self, nums: List[int]) -> int:
        # 直到子陣列分數不是零, 才停止切割
        # 被題目騙了, 以為 10^5, 會是 N * logN
        # 但實際上只要用貪婪, 循序尋找

        score = self.score(nums)
        if score != 0:
            return 1

        ans = 1
        cursor = 0
        size = len(nums)
        while cursor < size:
            idx = self.get_cut_index(nums[cursor:])
            if idx != -1:
                cursor = idx + 1
                ans += 1
            else:
                return ans
        return ans

    def get_cut_index(self, nums) -> int:
        cut_index = -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            print(mid)
            l_score = self.score(nums[:mid + 1])
            r_score = self.score(nums[mid + 1:])
            if l_score == r_score == 0:
                cut_index = mid
                r = mid - 1
            elif l_score == 0:
                r = mid - 1
            elif r_score == 0:
                l = mid + 1
        return cut_index


if __name__ == '__main__':
    print(Solution().maxSubarrays([1, 0, 2, 0, 1, 2]) == 3)
    print(Solution().maxSubarrays([100000]) == 1)
    print(Solution().maxSubarrays([8, 9]) == 1)
    print(Solution().maxSubarrays([0, 8, 0, 0, 0, 23]) == 4)
