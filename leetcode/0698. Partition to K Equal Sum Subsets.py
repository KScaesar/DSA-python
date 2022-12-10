from tool import *


class Bitmask:
    def __init__(self, n: int):
        self.mask: int = 0
        self.n: int = n

    def __cursor(self, index):
        shift = self.n - index - 1
        return 1 << shift

    def enable(self, index):
        self.mask |= self.__cursor(index)

    def cancel(self, index):
        # self.mask ^= self.__cursor(index)
        self.mask &= ~self.__cursor(index)

    def is_enable(self, index) -> bool:
        return True if self.mask & self.__cursor(index) else False

    def __str__(self):
        return f'{self.mask:0{self.n}b}'


class Solution:
    # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
    # https://hackmd.io/@sh1zuku/ByMaNphEv#Partition-to-K-Equal-Sum-Subsets
    # https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solutions/180014/backtracking-x-2/
    def canPartitionKSubsets_dp(self, nums: list[int], k: int) -> bool:
        pass

    def canPartitionKSubsets_backtrace(self, nums: list[int], k: int) -> bool:
        # backtrace 的思想
        # 分為兩種作法
        # 1. for each subset, put any numbers inside
        # 2. for each number, put it into any subset

        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) / k
        print(k, nums, target)
        subset = dict()

        def backtrace(nums, start, track, used, set_k) -> bool:
            nonlocal target, k, subset
            if set_k == k:
                return True

            subset_sum = sum([x[1] for x in track])
            if subset_sum > target:
                return False
            elif subset_sum == target:
                # print("index =", [x[0] for x in track])
                # print("num =", [x[1] for x in track])
                print(f'{set_k:>2} {start:>3} {used}')
                subset[set_k] = [x[1] for x in track]
                # print()

                # 注意是從 0 開始
                # 從剩下的數字, 看是否子集合符合目標
                # return backtrace(nums, start + 1, [], used, set_k + 1)
                return backtrace(nums, 0, [], used, set_k + 1)

            for i in range(start, len(nums)):
                if nums[i] > target:
                    return False

                # 重要加速判斷, 如果數字相同
                # i 已經作過類似判斷, 但是找不到解
                # i+1 不需要重複進行
                # if used[i]:
                #
                # if used[i] or (i > 0 and not used[i - 1] and nums[i] == nums[i - 1]):
                if used.is_enable(i) or (i > start and not used.is_enable(i - 1) and nums[i] == nums[i - 1]):
                    continue

                # used[i] = True
                used.enable(i)

                track.append((i, nums[i]))
                if backtrace(nums, i + 1, track, used, set_k):
                    track.pop()
                    return True
                track.pop()

                # used[i] = False
                used.cancel(i)

            return False

        # used = [False] * len(nums)
        used = Bitmask(len(nums))
        r = backtrace(nums, 0, [], used, 0)
        print(subset)
        return r

    def canPartitionKSubsets_fail3(self, nums: list[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)  # 要從最大的開始放, 不然空間先被小的佔據, 後面大的放不下去
        target = sum(nums) / k
        print(nums, target)

        @debug_helper
        def backtrace(nums, start, track, used):
            nonlocal k, target

            subset_sum = sum([nums[i] for i in track])
            if subset_sum > target:
                return
            elif subset_sum == target:
                for i in track:
                    if used[i]:
                        return
                for i in track:
                    used[i] = True
                k -= 1
                print([nums[i] for i in track])
                return

            for i in range(start, len(nums)):
                if nums[i] > target:
                    return
                track.append(i)
                backtrace(nums, i + 1, track, used)
                track.pop()

        backtrace(nums, 0, [], [False] * len(nums))
        return k == 0

    def canPartitionKSubsets_fail2(self, nums: list[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)  # 要從最大的開始放, 不然空間先被小的佔據, 後面大的放不下去
        target = sum(nums) / k

        def backtrace(nums, start, track, picked):
            nonlocal k, target

            subset_sum = sum([x[1] for x in track])
            # 子集合 是 回朔樹上所有節點, 不需要進行 start == len(nums) + 1 的判斷
            if start == len(nums) + 1 or subset_sum > target or k == 0:
                return

            if subset_sum == target:
                # 已經選擇的數字, 不需要繼續後面的流程
                #
                # 後來發現
                #
                # nums =   [5   , 4   , 3   , 3    , 2   , 2    , 1]
                # picked = [True, True, True, False, True, False, True]
                # picked[3]=False, nums[4] 卻是 True
                # 理論上不該選擇 這個子集合
                # 但卻更新了 picked[3]
                #
                # 更改作法為
                # 確定所有元素都合法
                # 在修改為 True
                # 不要邊確認 邊修改
                for i in [x[0] for x in track]:
                    if picked[i]:
                        return
                    picked[i] = True

                k -= 1
                print(track, k)
                print(f'{nums}\n{picked}\n')
                return

            for i in range(start, len(nums)):
                if nums[i] > target:
                    return

                track.append((i, nums[i]))
                backtrace(nums, i + 1, track, picked)
                track.pop()

        backtrace(nums, 0, [], [False] * len(nums))
        return k == 0

        pass

    def canPartitionKSubsets_fail1(self, nums: list[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) / k

        # print(nums, target)

        # @debug_helper
        def backtrace(nums, start, track):
            nonlocal k, target

            # 空集合本身 是 樹的根節點
            # 應該把結束條件看成
            # 當尋訪深度達到子葉終點才結束
            # 所以樹高是 nums + 空集合 的數量
            if start == len(nums) + 1 or sum(track) > target:
                return

            if sum(track) == target:
                if k == 0:
                    return
                # print(track)
                k -= 1  # 單純用 k 紀錄, 可能重複用同一個數字

            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrace(nums, i + 1, track)
                track.pop()

        backtrace(nums, 0, [])
        return k == 0


if __name__ == '__main__':
    # print(Solution().canPartitionKSubsets_fail1([4, 3, 2, 3, 5, 2, 1], 4), "\n")
    # print(Solution().canPartitionKSubsets_fail2([2, 2, 2, 2, 3, 4, 5], 4), "\n")
    # print(Solution().canPartitionKSubsets_fail3([10, 10, 10, 9, 9, 9, 8, 7, 6, 5, 5, 4, 4, 4, 3, 2], 5), "\n")

    # print(Solution().canPartitionKSubsets_backtrace([4, 3, 2, 3, 5, 2, 1], 4), "\n")
    # print(Solution().canPartitionKSubsets_backtrace([2, 2, 2, 2, 3, 4, 5], 4), "\n")
    # print(Solution().canPartitionKSubsets_backtrace([10, 10, 10, 9, 9, 9, 8, 7, 6, 5, 5, 4, 4, 4, 3, 2], 5), "\n")
    print(Solution().canPartitionKSubsets_backtrace([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10), "\n")
    # print(Solution().canPartitionKSubsets_backtrace([1, 1, 1], 3), "\n")
    # print(Solution().canPartitionKSubsets_backtrace([2, 2, 2, 2, 1, 1, 1, 1], 2), "\n")

    # print(Solution().canPartitionKSubsets_dp([1, 1, 1], 3), "\n")
