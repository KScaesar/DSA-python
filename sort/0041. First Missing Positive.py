from typing import List


class Solution:
    # https://leetcode.com/problems/first-missing-positive/

    # https://www.techiedelight.com/zh-tw/find-smallest-missing-positive-number-unsorted-array/
    # https://bclin.tw/2022/05/30/leetcode-41/

    # 我想到的方式
    # 1. 先找出 max, 把 1 ~ max 進行 xor, 得到所有元素的集合
    # 2. 把 nums 的正數 進行 xor, 得到已存在元素的集合
    # 3. 把第 1, 2 步驟 的集合進行 xor, 得到缺失元素的集合
    # 4. 之後想不到辦法, 如何利用缺失元素的集合

    def firstMissingPositive(self, nums: List[int]) -> int:
        # 使用 Quicksort 的 Partitioning
        # 使用 0 作為樞軸元素並進行一次分區過程。
        # 在分區步驟之後，所有正數都放在數組的一側

        size = len(nums)

        # 注意 partition 會改變 nums input 的內容
        idx_of_last_positive_number = partition_positive_number(nums, size)
        cnt_of_positive_number = idx_of_last_positive_number + 1

        # 使用類似 cyclic sort 的作法
        # A[A[i] - 1]
        for i in range(cnt_of_positive_number):
            idx = abs(nums[i]) - 1
            if idx < cnt_of_positive_number and nums[idx] >= 0:
                nums[idx] = -nums[idx]

        # 案例 1. 缺失的數字在 1 到 k 的範圍內
        for i in range(cnt_of_positive_number):
            if nums[i] > 0:
                return i + 1

        # 案例 2. 如果數組中存在從 1 到 k 的數字，
        # 那麼缺失的數字是 `k + 1` 例如 [1, 2, 3, 4] —> 5
        return cnt_of_positive_number + 1


# partition swap 解說
# https://rust-algo.club/sorting/quicksort/index.html#%E8%AA%AA%E6%98%8E

def partition_positive_number(nums: list[int], size: int) -> int:
    pivot = 0
    slow, fast = -1, 0

    while fast < size:
        if nums[fast] <= pivot:  # 令 pivot 左邊為正, 右邊為負, 這樣 return index 剛好可以當成 counter 使用
            fast += 1
        else:
            slow += 1
            nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1

    return slow


if __name__ == '__main__':
    print(Solution().firstMissingPositive([1, 2, 1, 0]))
    print(Solution().firstMissingPositive([-1, -2, -1]))
    print(Solution().firstMissingPositive([2, 1, 2, 4]))
    print(Solution().firstMissingPositive([2, 1, -2, 4]))
