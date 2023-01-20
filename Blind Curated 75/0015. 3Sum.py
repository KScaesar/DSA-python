from typing import List


class Solution:
    # https://leetcode.com/problems/3sum/

    # https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.md

    def threeSum_v4(self, nums: List[int]) -> List[List[int]]:
        # 重點之一, nums 有多對元素和 且 不可以重複, 應該如何處理
        # 算法筆記 p328

        nums.sort()
        ans = []
        target = 0
        print(nums)

        # for i in range(0, len(nums), 1):
        #
        # python for range 的 規則
        # 和其他語言不一樣 for i=0 ; ; i++
        # 在 python 即使 在 迴圈內
        # 把 i 加到 100
        # 下一個 i 依然會按照 range 所定義的 step
        # 只前進 1
        i = 0
        while i < len(nums):
            v = nums[i]

            # three sum 避免重複的考量設計 1 - 寫法2
            # 和寫法1的差異 以及 程式碼位置 要特別注意
            # while i > 0 and nums[i] == nums[i - 1]:
            #     i += 1

            # three sum 避免重複的考量設計 2
            # 由於 two sum 已經可以求出 多組不重複解
            # 所以 three sum 不需要每次掃描 所有的元素
            r = self.twoSum_v3(nums, target - v, i + 1)
            print(f'i={i} v={v} r={r}')
            for item in r:
                ans.append([v, *item])

            # three sum 避免重複的考量設計 1 - 寫法1
            # 記得考慮邊界
            #
            # while i < len(nums) and nums[i] == v:
            # 如果使用 two sum 的 避免重複條件
            # 會多前進一格
            # 因為 for i=0 ; ; i++ 本身就會前進
            #
            # 沒有規定 跳過重複的程式
            # 不能用在 for i=0 ; ; i++
            # 但是判斷條件 不太一樣
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            i += 1

        return ans

    def twoSum_v3(self, nums, target, start) -> list[list[int]]:
        # 找出多個組合的版本
        # 且要避免重複
        # 而不是找出單一解就回傳
        # 本題重點是 跳過重複 有怎樣的實做方式

        nums.sort()  # 沒進行排序的話, 很難最佳化 過濾重複 的問題

        lo = start
        hi = len(nums) - 1
        ans = []

        # while lo <= hi:
        # 條件不應該有 等於
        # 因為要求 sum 累加的元素, 不能是同一個
        # 等號的情況, 代表指向同一個元素, 違反題目規則
        while lo < hi:
            lo_v = nums[lo]
            hi_v = nums[hi]
            _sum = lo_v + hi_v
            # print(f' num[{lo:>1}]={lo_v} num[{hi:>1}]={hi_v}')
            if _sum == target:
                ans.append([lo_v, hi_v])

                # 為了找到下一個解, 可以選擇 lo or hi 到下一個元素
                while hi >= 0 and hi_v == nums[hi]:  # 跳過重複
                    hi -= 1

                # 此區塊是可忽略的
                # 可以少一次 sum 的計算
                #
                # while lo_v == nums[lo]:  # 跳過重複
                #     lo += 1
            elif _sum > target:
                while hi >= 0 and hi_v == nums[hi]:  # 跳過重複 記得要確保 index 在邊界內
                    hi -= 1
            elif _sum < target:
                while lo < len(nums) and lo_v == nums[lo]:  # 跳過重複
                    lo += 1

        return ans

    def threeSum_fail_v3(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = dict()

        for i in range(len(nums)):
            target = nums[i]

            nums.pop(i)

            # 失敗原因
            # nums 中, 可能有多組解 可以得到 target
            # 但是在 two sum, 總是在找到第一組解, 就返回
            two_result = self.twoSum_v2(nums, -target)
            if two_result:
                r = [target, *two_result]
                r.sort()
                if tuple(r) not in used:
                    used[tuple(r)] = True
                    ans.append(r)

            nums.insert(i, target)

        return ans

    def twoSum_v2(self, nums, target) -> list[int] | None:
        memo = dict()
        for i in range(len(nums)):
            if nums[i] not in memo:
                memo[target - nums[i]] = True
            else:
                return [target - nums[i], nums[i]]
        return None

    def threeSum_fail_v2(self, nums: List[int]) -> List[List[int]]:
        # 失敗原因
        # 排序後 往後找其他配對元素
        # 是錯誤的想法
        # 只能找出部份解

        nums.sort()
        ans = []
        used = dict()
        print(nums)

        for i in range(len(nums)):
            target = nums[i]

            # +1 是為了跳過 target 本身, 找其他配合的元素
            # 且因為 nums 已經排序, 往後找可以確保一定會是不同的結果
            sub_result = self.twoSum_v1(nums, -target, i + 1)
            if sub_result:
                r = [target, *sub_result]
                if tuple(r) in used:
                    continue

                used[tuple(r)] = True
                ans.append(r)

        return ans

    def threeSum_fail_v1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        used = dict()
        print(nums)

        for i in range(len(nums)):
            target = nums[i]

            # 避免同樣的目標值 重複尋找
            if target in used:
                continue
            used[target] = True

            # +1 是為了跳過 target 本身, 找其他配合的元素
            # 且因為 nums 已經排序, 往後找可以確保一定會是不同的結果
            sub_result = self.twoSum_v1(nums, -target, i + 1)
            if sub_result:
                ans.append([target, *sub_result])

        return ans

    def twoSum_v1(self, nums, target, start) -> list[int] | None:
        memo = dict()
        for i in range(start, len(nums)):
            if nums[i] not in memo:
                memo[target - nums[i]] = True
            else:
                return [target - nums[i], nums[i]]
        return None


if __name__ == '__main__':
    print(f'{Solution().threeSum_v4([-1, 0, 1, 2, -1, -4])}')
    print(f'{Solution().twoSum_v3([1, 3, 1, 2, 2, 3], 4, 0)}')
