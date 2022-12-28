from typing import List


class Solution:
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

    # 類似題目
    # 0034. Find First and Last Position of Element in Sorted Array
    def findMin(self, nums: List[int]) -> int:
        # 此解法只能用在 數字不重複出現
        # 例如: [1 2 3 3 4] -> [3 4 1 2 3] , 破壞了 check 特性
        # 左邊區段 也可能 滿足不變特性 nums[mid] <= nums[-1]
        #
        # https://zhuanlan.zhihu.com/p/259545903
        # 可以看看 若會同樣的數字重複出現, 寫法是怎麼樣的

        left = 0
        right = len(nums) - 1
        while left < right:  # 停止的時候, 只剩下一個元素
            mid = (left + right) // 2

            # 解讀為 mid 右邊(包含mid) 都滿足條件
            # 就更新右邊
            #
            # 為什麼用這個條件, 因為很明顯
            # 最小值存在的區段, 都滿足這個條件
            if nums[mid] <= nums[-1]:
                right = mid  # 答案可能包含在其中, 所以不能排除 mid, 因此不需要 -1
            else:
                left = mid + 1
        return nums[left]

    def findMax(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # 解讀為 mid 左邊(包含mid) 都滿足條件
            # 就更新左邊
            #
            # 為什麼用這個條件, 因為很明顯
            # 最大值存在的區段, 都滿足這個條件
            if nums[mid] >= nums[0]:
                left = mid  # 答案可能包含在其中, 所以不能排除 mid, 因此不需要 +1
            else:
                right = mid - 1
        return nums[left]


if __name__ == '__main__':
    print(Solution().findMin([3, 4, 5, 1, 2]))
    print(Solution().findMax([3, 4, 5, 1, 2]))
